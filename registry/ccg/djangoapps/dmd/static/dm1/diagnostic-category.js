django.jQuery(function () {
    var $ = django.jQuery;

    // Retrieve the top-level fieldset for the inline.
    var fs = $("div[id^='diagnosticcategory']:not(.empty-form) > fieldset");

    if (fs.length != 1) {
        /* Not much we can do if we can't find the right fieldset,
         * realistically. No point informing the user, since it's unlikely
         * they'll care, so we'll log it to the console if one's available and
         * get out. */
        if ("console" in window) {
            window.console.log("Error getting diagnostic category fieldset; cannot continue.");
            return;
        }
    }

    // Only show the repeat size element when certain categories are selected.
    var category = $("div.category select", fs);
    var repeatSizeContainer = $("div.repeat_size", fs);
    var categoryOnChange = function () {
        if (category.val().indexOf("positive") != -1) {
            repeatSizeContainer.show();
        }
        else {
            repeatSizeContainer.hide();
        }
    };

    category.change(categoryOnChange);
    categoryOnChange();

    /* Similarly, only show the relative CTG/CCTG repeat elements if the
     * relative has been DNA tested in the first place. */
    var relative = $("div.relative_test input", fs);
    var relativeRepeatContainers = $("div.relative_ctg_repeat, div.relative_cctg_repeat", fs);
    var relativeOnChange = function () {
        if (relative.attr("checked")) {
            relativeRepeatContainers.show();
        }
        else {
            relativeRepeatContainers.hide();
        }
    };

    relative.change(relativeOnChange);
    relativeOnChange();
});
