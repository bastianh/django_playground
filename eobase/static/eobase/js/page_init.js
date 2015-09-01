$(document).on("ready", function () {
    var $loading = $('#ajax_spinner');
    $(document)
        .pjax('[data-pjax] a, a[data-pjax]', '#pjax', {timeout: 2000, maxCacheLength: 0})
        .ajaxStart(function () {
            $loading.show()
        })
        .ajaxStop(function () {
            $loading.hide()
        });
    swampdragon.ready(function () {
        console.log("sd ready");
        swampdragon.callRouter('get_date', 'foo', {value: 10}, function (context, data) {
            console.log("r", data);
        });
    });
    swampdragon.open(function () {
        console.log("sd open");
    });
    swampdragon.close(function () {
        console.log("sd close");
    });
    console.log("setup");
});

/*
 $(document).on("pjax:success", function () {

 });
 */
