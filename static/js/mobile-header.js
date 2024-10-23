$(document).ready(function () {
    $('.header-mb').hide()
    $('.header-control').click(function () {
        $('.header-mb').slideToggle()
        if (  $( this ).css( "transform" ) == 'none' ){
            $(this).css("transform","rotate(180deg)");
         } else {
            $(this).css("transform","" );
    }
    })

})