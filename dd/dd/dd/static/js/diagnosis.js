$(document).ready(function() {
    $('.field-treatment_other').hide();
    $('.field-condition_other').hide();
    
    if ($('#id_treatmentcourse_set-0-treatment option:selected').text() == 'Other') {
        $('.field-treatment_other').toggle('fast');
    }

    if ($('#id_diagnosis option:selected').text() == 'Other') {
        $('.field-condition_other').toggle('fast');
    }
    
    $('#id_treatmentcourse_set-0-treatment').on('change', function() {
        if ($(this).find("option:selected").text() == 'Other') {
            $('.field-treatment_other').show('fast');
        } else {
            $('.field-treatment_other').hide('fast');
        }
    })
    
    $('#id_diagnosis').on('change', function() {
        if ($(this).find("option:selected").text() == 'Other') {
            $('.field-condition_other').show('fast');
        } else {
            $('.field-condition_other').hide('fast');
        }
    })
});