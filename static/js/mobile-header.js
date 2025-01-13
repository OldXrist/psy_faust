$(document).ready(function () {
    $('.header-mb').hide()
    $('.header-control svg').click(function () {
        $('.header-mb').slideToggle()
        if (  $( this ).css( "transform" ) == 'none' ){
            $(this).css("transform","rotate(180deg)");
         } else {
            $(this).css("transform","" );
    }
    })
    $('.header-mb-links .nav-link, .header-mb-container .btn').click(function () {
        $('.header-mb').slideToggle()
        if (  $('.header-control svg').css( "transform" ) == 'none' ){
            $('.header-control svg').css("transform","rotate(180deg)");
         } else {
            $('.header-control svg').css("transform","" );
    }
    })
})