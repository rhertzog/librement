$.extend({
  feature: function(body_class,callback) {
    if ($('body').hasClass(body_class)) {
      $(callback);
    }
  },
  focus_first_of: function() {
    for (var i = 0; i < arguments.length; i++) {
      var elem = $(arguments[i]);

      if (elem.length === 0 || elem.val().length !== 0) {
        continue;
      }

      elem.focus();
      return;
    }
  }
});

$.feature('f_profile', function() {
  var container = $('.rss');

  if (!container.data('url')) {
    return;
  }

  $.get(container.data('url'), function(html) {
    container.replaceWith(html);
  });
});
