import os
import Image
import StringIO

from django.db import models
from django.utils.crypto import get_random_string
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile

class YADTImageField(object):
    def __init__(self, variants=None, cachebust=False):
        self.variants = variants or {}
        self.cachebust = cachebust

        for name, config in self.variants.iteritems():
            if name == 'original':
                raise ValueError("'original' is a reserved variant name")

            if config['format'] not in ('jpeg', 'png'):
                raise ValueError(
                    "'%s' is not a valid format" % config['format']
                )

        self.variants['original'] = {
            'format': 'jpeg',
            'original': True,
        }

    def contribute_to_class(self, cls, name):
        self.model = cls
        self.name = name
        self.cachebusting_field = None

        self.upload_to = os.path.join(
            'yadt',
            '%s.%s' % (
                self.model._meta.app_label,
                self.model._meta.object_name,
            ),
            self.name,
        )

        if self.cachebust:
            self.cachebusting_field = models.CharField(
                max_length=8,
                default='',
            )

            cls.add_to_class(
                '%s_hash' % name,
                self.cachebusting_field,
            )

        cls._meta.add_virtual_field(self)

        setattr(cls, name, Descriptor(self))

class Descriptor(object):
    def __init__(self, field):
        self.field = field

    def __get__(self, instance=None, owner=None):
        if instance is None:
            return YADTClassImage(self.field)

        return YADTImage(self.field, instance)

##

class YADTImage(object):
    def __init__(self, field, instance):
        self.field = field
        self.instance = instance
        self.variants = {}

        for name, config in self.field.variants.iteritems():
            self.variants[name] = YADTImageFile(name, config, self, instance)
        self.__dict__.update(self.variants)

        # Convenience methods
        for x in ('url', 'save', 'open', 'exists'):
            setattr(self, x, getattr(self.original, x))

    def __repr__(self):
        return u"<YADTImage: %s.%s.%s (%s)>" % (
            self.field.model._meta.app_label,
            self.field.model._meta.object_name,
            self.field.name,
            self.field.upload_to,
        )

    def refresh(self):
        for variant in self.variants.values():
            if not variant.config.get('original', False):
                variant.refresh()

    def cachebust(self):
        if self.field.cachebusting_field:
            return setattr(
                self.instance,
                self.field.cachebusting_field.name,
                get_random_string(self.field.cachebusting_field.max_length),
            )

class YADTImageFile(object):
    def __init__(self, name, config, image, instance):
        self.name = name
        self.image = image
        self.config = config
        self.instance = instance

        self.filename = os.path.join(
            self.image.field.upload_to,
            self.name,
            '%d.%s' % (self.instance.pk, self.config['format']),
        )

    def __repr__(self):
        return u"<YADTImageFile: %s>" % self.filename

    @property
    def url(self):
        url = default_storage.url(self.filename)

        if self.image.field.cachebusting_field:
            suffix = getattr(
                self.instance,
                self.image.field.cachebusting_field.name,
            )

            if suffix:
                url += '?%s' % suffix

        return url

    def exists(self):
        return default_storage.exists(self.filename)

    def save(self, content):
        default_storage.delete(self.filename)

        filename = default_storage.save(self.filename, content)

        assert filename == self.filename, \
            "Image was not stored at the location we wanted"

        if self.config.get('original', False):
            self.image.refresh()

        self.image.cachebust()

    def open(self, mode='rb'):
        return default_storage.open(self.filename)

    def refresh(self):
        if self.config.get('original', False):
            raise NotImplementedError("Cannot refresh the original image")

        im = Image.open(self.image.original.open())

        if 'width' in self.config and 'height' in self.config:
            if self.config.get('crop', False):
                src_width, src_height = im.size

                src_ratio = float(src_width) / float(src_height)
                dst_ratio = float(self.config['width']) / float(self.config['height'])

                if dst_ratio < src_ratio:
                    crop_height = src_height
                    crop_width = crop_height * dst_ratio
                    x_offset = int(float(src_width - crop_width) / 2)
                    y_offset = 0
                else:
                    crop_width = src_width
                    crop_height = crop_width / dst_ratio
                    x_offset = 0
                    y_offset = int(float(src_height - crop_height) / 3)

                im = im.crop((
                    x_offset,
                    y_offset,
                    x_offset + int(crop_width),
                    y_offset + int(crop_height))
                )

                im = im.resize(
                    (self.config['width'], self.config['height']),
                    Image.ANTIALIAS,
                )
            else:
                im.thumbnail(
                    (self.config['width'], self.config['height']),
                    Image.ANTIALIAS,
                )

        fileobj = StringIO.StringIO()
        im.save(fileobj, self.config['format'])

        self.save(InMemoryUploadedFile(
            fileobj,
            None,
            self.filename,
            'application/octet-stream',
            fileobj.len,
            None,
        ))

##

class YADTClassImage(object):
    def __init__(self, field):
        self.field = field

        self.variants = {}

        for name, config in self.field.variants.iteritems():
            self.variants[name] = YADTClassVariant(name, config, self)
        self.__dict__.update(self.variants)

    def __repr__(self):
        return u"<YADTClassImage: %s.%s.%s (%s)>" % (
            self.field.model._meta.app_label,
            self.field.model._meta.object_name,
            self.field.name,
            self.field.upload_to,
        )

class YADTClassVariant(object):
    def __init__(self, name, config, image):
        self.name = name
        self.image = image
        self.config = config

    def refresh_all(self, generator=False):
        if self.config.get('original', False):
            raise NotImplementedError("Cannot refresh the original image")

        for instance in self.image.field.model.objects.all():
            image = getattr(instance, self.image.field.name)

            if image.original.exists():
                getattr(image, self.name).refresh()

            yield image

        if self.image.field.cachebusting_field:
            field = self.image.field.cachebusting_field

            field.model.objects.update(**{
                field.name: get_random_string(field.max_length)
            })

    def cachebust(self):
        if self.field.cachebusting_field:
            return setattr(
                self.instance,
                self.field.cachebusting_field.name,
                get_random_string(self.field.cachebusting_field.max_length),
            )

