let countySelected = $('#id_default_county').val();
if (!countySelected) {
    $ ('#id_default_county').css('color', '#aab7c4');
};
$ ('#id_default_county').change(function() {
    countySelected = $(this).val();
    if (!countySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});
