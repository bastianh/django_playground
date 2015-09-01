from django_assets import Bundle, register

css = Bundle(
    'eobase/static/eobase/scss/app.scss',
    filters='scss', output='static/gen/packed.css')

register('css_all', css)

js = Bundle(
    # 'eobase/static/bower_components/modernizr/modernizr.js',
    'eobase/static/bower_components/jquery/dist/jquery.js',
    # 'eobase/static/bower_components/toastr/toastr.js',
    "eobase/static/bower_components/bootstrap-sass/assets/javascripts/bootstrap/tooltip.js",
    "eobase/static/bower_components/bootstrap-sass/assets/javascripts/bootstrap/affix.js",
    "eobase/static/bower_components/bootstrap-sass/assets/javascripts/bootstrap/alert.js",
    "eobase/static/bower_components/bootstrap-sass/assets/javascripts/bootstrap/button.js",
    "eobase/static/bower_components/bootstrap-sass/assets/javascripts/bootstrap/carousel.js",
    "eobase/static/bower_components/bootstrap-sass/assets/javascripts/bootstrap/collapse.js",
    "eobase/static/bower_components/bootstrap-sass/assets/javascripts/bootstrap/dropdown.js",
    "eobase/static/bower_components/bootstrap-sass/assets/javascripts/bootstrap/modal.js",
    "eobase/static/bower_components/bootstrap-sass/assets/javascripts/bootstrap/popover.js",
    "eobase/static/bower_components/bootstrap-sass/assets/javascripts/bootstrap/scrollspy.js",
    "eobase/static/bower_components/bootstrap-sass/assets/javascripts/bootstrap/tab.js",
    "eobase/static/bower_components/bootstrap-sass/assets/javascripts/bootstrap/transition.js",
    'eobase/static/bower_components/jquery-pjax/jquery.pjax.js',
    'eobase/static/eobase/js/page_init.js',
    filters='uglifyjs', output='static/gen/main.js')

register('js_all', js)
