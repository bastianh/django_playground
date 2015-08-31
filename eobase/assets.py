from django_assets import Bundle, register

css = Bundle(
    'eobase/static/bower_components/foundation/css/normalize.css',
    'eobase/static/eobase/scss/app.scss',
    filters='scss', output='gen/packed.css')

register('css_all', css)

js = Bundle(
    'eobase/static/bower_components/modernizr/modernizr.js',
    'eobase/static/bower_components/jquery/dist/jquery.js',
    'eobase/static/bower_components/toastr/toastr.js',
    'eobase/static/bower_components/foundation/js/foundation/foundation.js',
    'eobase/static/bower_components/foundation/js/foundation/foundation.topbar.js',
    'eobase/static/bower_components/foundation/js/foundation/foundation.tooltip.js',
    'eobase/static/bower_components/foundation/js/foundation/foundation.reveal.js',
    'eobase/static/bower_components/foundation/js/foundation/foundation.offcanvas.js',
    'eobase/static/bower_components/jquery-pjax/jquery.pjax.js',
    'eobase/static/eobase/js/page_init.js',
    filters='uglifyjs', output='gen/main.js')

register('js_all', js)
