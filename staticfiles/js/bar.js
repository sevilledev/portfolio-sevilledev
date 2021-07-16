$('.bar-btn').click(function(){
    $('header').addClass('open-menu');
    $('.btn').css({"left": '260px'});
    $(this).hide()
    $('.bar-btn-close').show()
});

$('.bar-btn-close').click(function(){
    $('header').removeClass('open-menu');
    $('.btn').css({"left": '0px'});
    $(this).hide()
    $('.bar-btn').show()
})

