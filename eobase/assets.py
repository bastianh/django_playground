from django_assets import Bundle, register

css = Bundle(
    'eobase/static/bower_components/foundation/css/normalize.css',
    'eobase/static/eobase/scss/app.scss',
    filters='scss', output='gen/packed.css')

register('css_all', css)

js = Bundle(
    'bower_components/modernizr/modernizr.js',
    'bower_components/jquery/dist/jquery.js',
    'bower_components/toastr/toastr.js',
    'bower_components/foundation/js/foundation/foundation.js',
    'bower_components/foundation/js/foundation/foundation.topbar.js',
    'bower_components/foundation/js/foundation/foundation.tooltip.js',
    'bower_components/foundation/js/foundation/foundation.reveal.js',
    'bower_components/foundation/js/foundation/foundation.offcanvas.js',
    'bower_components/jquery-pjax/jquery.pjax.js',
    'eobase/static/eobase/js/page_init.js',
    filters='uglifyjs', output='gen/main.js')

register('js_all', js)
