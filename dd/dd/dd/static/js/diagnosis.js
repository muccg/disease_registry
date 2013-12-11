$(document).ready(function() {
    $('.field-treatment_other').hide();
    
    if ($('#id_treatmentcourse_set-0-treatment option:selected').text() == 'Other') {
        $('.field-treatment_other').toggle('fast');
    }
    
    $('#id_treatmentcourse_set-0-treatment').on('change', function() {
        if ($(this).find("option:selected").text() == 'Other') {
            $('.field-treatment_other').show('fast');
        } else {
            $('.field-treatment_other').hide('fast');
        }
    })
});