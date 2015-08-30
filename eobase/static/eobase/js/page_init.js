// als letztes file nach allen anderen javascript libraries

$(document).on("ready", function(){

    var _canvas = Foundation.utils.S('[data-offcanvas]');
    Foundation.utils.S("#offcanvas_toggle").on('click', function (e) {
        _canvas.foundation('offcanvas', 'toggle', 'move-right');
    });

    $(window).on('resize', Foundation.utils.throttle(function (e) {
        if (Foundation.utils.is_medium_up()) {
            if (_canvas.hasClass("move-right")) {
                _canvas.foundation('offcanvas', 'hide', 'move-right');
            }
        }
    }, 300));

    $(document)
        .foundation()
        .pjax('[data-pjax] a, a[data-pjax]', '#pjax-container');


});


