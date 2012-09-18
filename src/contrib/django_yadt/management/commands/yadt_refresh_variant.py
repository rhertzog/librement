import sys

from django.db import models
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    USAGE = "<app_label> <model> <field> <variant>"

    def handle(self, *args, **options):
        try:
            app_label, model_name, field_name, variant_name = args
        except ValueError:
            raise CommandError(self.USAGE)

        model = models.get_model(app_label, model_name)

        if model is None:
            raise CommandError("%s.%s is not a valid model name" % (
                app_label,
                model_name,
            ))

        try:
            field = getattr(model, field_name)
        except AttributeError:
            raise CommandError("%s.%s has no field %s" % (
                app_label,
                model_name,
                field_name,
            ))

        try:
            variant = getattr(field, variant_name)
        except AttributeError:
            raise CommandError("%s.%s.%s has no variant %s" % (
                app_label,
                model_name,
                field_name,
                variant_name,
            ))

        for x in variant.refresh_all(generator=True):
            sys.stderr.write('.')
        sys.stderr.write('\n')
