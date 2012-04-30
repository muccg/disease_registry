/* Stock function to create an XMLHttpRequest object in a cross-browser way:
 * for most browsers these days that just means instantiating the object, but
 * older IE versions require a little more magic. */
var XHR = {
    create: function () {
        if (typeof XMLHttpRequest == "undefined") {
            try {
                return new ActiveXObject("Msxml2.XMLHTTP.6.0");
            }
            catch (e) {}

            try {
                return new ActiveXObject("Msxml2.XMLHTTP.3.0");
            }
            catch (e) {}

            try {
                return new ActiveXObject("Msxml2.XMLHTTP");
            }
            catch (e) {}

            throw new Error("Cannot create an XMLHttpRequest object");
        }
        else {
            return new XMLHttpRequest();
        }
    }
};


// vim: set cin ai et ts=4 sw=4:
