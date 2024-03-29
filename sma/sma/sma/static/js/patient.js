(function() {
    var init = function() {
        /* This is pretty ugly, and pretty specific to how Django Admin builds
         * forms. */

        // First up, we'll find the next of kin address.
        var address;

        if (document.querySelector) {
            address = document.querySelector("div.next_of_kin_address");
        }
        else {
            var divs = document.getElementsByTagName("div");

            for (var i = 0; i < divs.length; i++) {
                var div = divs[i];

                if (div.className.indexOf("next_of_kin_address") != -1) {
                    address = div;
                }
            }
        }

        if (address) {
            /* Right, now we'll create a new row within the table and wire up
             * an event handler to copy the relevant fields. */
            var div = document.createElement("div");
            div.className = "form-row no-print";

            var link = document.createElement("a");
            link.href = "#";
            link.appendChild(document.createTextNode("Copy contact details from patient"));
            link.onclick = function() {
                /* An object with the IDs of the elements to copy as the keys
                 * and the IDs to copy to as values. */
                var copy = {
                    "id_address": "id_next_of_kin_address",
                    "id_suburb": "id_next_of_kin_suburb",
                    "id_state": "id_next_of_kin_state",
                    "id_postcode": "id_next_of_kin_postcode",
                    "id_home_phone": "id_next_of_kin_home_phone",
                    "id_mobile_phone": "id_next_of_kin_mobile_phone",
                    "id_work_phone": "id_next_of_kin_work_phone",
                    "id_email": "id_next_of_kin_email"
                };

                for (var sourceID in copy) {
                    if (copy.hasOwnProperty(sourceID)) {
                        var source = document.getElementById(sourceID);
                        var destination = document.getElementById(copy[sourceID]);

                        if (source && destination) {
                            destination.value = source.value;
                        }
                    }
                }

                return false;
            };

            div.appendChild(document.createElement("label"));
            div.appendChild(link);
            address.parentNode.insertBefore(div, address);
        }
    };

    // Handle existing onload handlers gracefully.
    if (window.onload) {
        var onload = window.onload;

        window.onload = function() {
            onload();
            init();
        };
    }
    else {
        window.onload = init;
    }
})();


// vim: set cin ai et ts=4 sw=4:
