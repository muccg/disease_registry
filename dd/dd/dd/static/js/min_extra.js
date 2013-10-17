/*
 * Django admin doesn't support a minimum number of inline forms.
 *
 * This code fixes up inline forms so that there is either a filled-in
 * inline form, or an empty inline form.
 *
 * To use this, set extra=0 on the inline forms.
 */

(function($) {
  "use strict";

  // window.load event is used because it occurs after the links are
  // set up by the document.ready handler in inlines.js.
  $(window).load(function() {
    var inline_is_empty = function() {
      var $related = $(this).children("div.inline-related");
      if ($related.not(".tabular").length == 0) {
        // check for empty TabularInline
        return $related.find(".form-row").not(".empty-form").length == 0;
      } else {
        // check for empty StackedInline
        return $related.not(".empty-form").length == 0;
      }
    };

    // trigger the "click" event on "Add another Object" links
    $(".inline-group")
      .filter(inline_is_empty)
      .find(".add-row a")
      .click();
  });
})(django.jQuery);
