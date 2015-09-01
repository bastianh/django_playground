$(document).on("ready", function () {
    var $loading = $('#ajax_spinner');
    $(document)
        .pjax('[data-pjax] a, a[data-pjax]', '#pjax-container', {timeout: 2000})
        .ajaxStart(function () {
            $loading.show()
        })
        .ajaxStop(function () {
            $loading.hide()
        });
});

$(document).on("pjax:success", function () {
    console.debug("pjax:success");
});


