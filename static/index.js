$(document).ready(function() {
    $('.form-check-input').off().on('click', function (e) {
        let $currentCheckbox = $(e.target);
        $currentCheckbox.closest('tr').find('.form-check-input').prop('checked', false);
        $currentCheckbox.prop('checked', true);
    });

    $("[data-toggle='tooltip']").tooltip();
        

    $('form').on('submit', function (e) {
        let parameters = [];
        let errorFlag = false;
        let $selects = $('.form-select');

        $selects.each(function () {
            if ($(this).val() == null) {
                $(this).addClass('invalid');
                errorFlag = true;
            }
            else {
                parameters.push($(this).val());
                $(this).removeClass('invalid');                
            }
        });

        let $tableRows = $('table tbody tr');

        $tableRows.each(function () {
            if ($(this).find('.form-check-input:checked').length == 0) {
                $(this).find('.fa-exclamation-circle').removeClass('d-none');
                errorFlag = true;
            }
            else {
                parameters.push($(this).find('.form-check-input:checked').attr('data-value'));
                $(this).find('.fa-exclamation-circle').addClass('d-none');
            }
        });
        
        if (errorFlag) {
            $('.alert').removeClass('d-none');
            setTimeout(function () {$('.alert').addClass('d-none')}, 3000);
            e.stopPropagation();
            e.preventDefault();
        }
        else {
            $('.alert').addClass('d-none');
        }
    });
});