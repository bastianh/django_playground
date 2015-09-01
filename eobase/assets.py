from django_assets import Bundle, register

css = Bundle('eobase/scss/app.scss', filters='scss,cssmin', output='css/packed.css')

register('css_all', css)

js = Bundle(
    # 'eobase/static/bower_components/modernizr/modernizr.js',
    'bower_components/jquery/dist/jquery.js',
    # 'eobase/static/bower_components/toastr/toastr.js',
    'bower_components/bootstrap-sass/assets/javascripts/bootstrap/tooltip.js',
    'bower_components/bootstrap-sass/assets/javascripts/bootstrap/affix.js',
    'bower_components/bootstrap-sass/assets/javascripts/bootstrap/alert.js',
    'bower_components/bootstrap-sass/assets/javascripts/bootstrap/button.js',
    'bower_components/bootstrap-sass/assets/javascripts/bootstrap/carousel.js',
    'bower_components/bootstrap-sass/assets/javascripts/bootstrap/collapse.js',
    'bower_components/bootstrap-sass/assets/javascripts/bootstrap/dropdown.js',
    'bower_components/bootstrap-sass/assets/javascripts/bootstrap/modal.js',
    'bower_components/bootstrap-sass/assets/javascripts/bootstrap/popover.js',
    'bower_components/bootstrap-sass/assets/javascripts/bootstrap/scrollspy.js',
    'bower_components/bootstrap-sass/assets/javascripts/bootstrap/tab.js',
    'bower_components/bootstrap-sass/assets/javascripts/bootstrap/transition.js',
    'swampdragon/js/dist/swampdragon.min.js',
    'bower_components/jquery-pjax/jquery.pjax.js',
    'eobase/js/page_init.js',
    filters='uglifyjs', output='js/main.js')

register('js_all', js)
