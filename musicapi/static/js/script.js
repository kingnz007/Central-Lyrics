
$(document).ready(function() {
    //click event on search icon
    $('#searchIcon, #close').click(searchIconClick);
});

function searchIconClick() {
    //css
    $('.form-wrapper').css({
        'width': '90%',
        'margin-right': '0',
        'padding': '10px',
        'position': 'absolute',
        'top': '-12%',
        'left': '0',
    });
    //y margin
    $('#searchButton').removeClass('my-2');
    //hide and display search bar
    $('.form-wrapper').toggle();
    //autofocus on input field
    $('#searchField').trigger('focus');
    //toggle close icon
    $('#close').toggleClass('d-none');
};
