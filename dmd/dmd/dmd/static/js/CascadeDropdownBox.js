$(document).ready(function() {
    $('#id_orpha').change(function() {
        _orpha = $(this).val();
        $.getJSON("/get_disease/"+ _orpha,
            function(ret, textStatus) {
                $('#id_disease').val(ret['disease_name']);
                get_disability(_orpha);
            }
        );
    });
    
    function get_disability(orpha) {
        $.getJSON("/get_disability/"+ _orpha,
            function(ret, textStatus) {
                $.each(ret, function(val, text) {
                    $('#id_disability').append(new Option(text.disability, val.disability));
                });
            }
        );
    }
});