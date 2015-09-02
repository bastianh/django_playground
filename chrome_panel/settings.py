from __future__ import absolute_import, unicode_literals

from django.conf import settings
from importlib import import_module


def is_middleware_class(middleware_class, middleware_path):
    # This could be replaced by import_by_path in Django >= 1.6.
    try:
        mod_path, cls_name = middleware_path.rsplit('.', 1)
        mod = import_module(mod_path)
        middleware_cls = getattr(mod, cls_name)
    except (AttributeError, ImportError, ValueError):
        return
    return issubclass(middleware_cls, middleware_class)


def is_toolbar_middleware_installed():
    from chrome_panel.middleware import ChromePanelMiddleware
    return any(is_middleware_class(ChromePanelMiddleware, middleware)
               for middleware in settings.MIDDLEWARE_CLASSES)


def prepend_to_setting(setting_name, value):
    """Insert value at the beginning of a list or tuple setting."""
    values = getattr(settings, setting_name)
    # Make a list [value] or tuple (value,)
    value = type(values)((value,))
    setattr(settings, setting_name, value + values)


def patch_middleware_classes():
    if not is_toolbar_middleware_installed():
        prepend_to_setting('MIDDLEWARE_CLASSES',
                           'chrome_panel.middleware.ChromePanelMiddleware')


def patch_root_urlconf():
    from django.conf.urls import include, url
    from django.core.urlresolvers import clear_url_caches, reverse, NoReverseMatch
    import chrome_panel
    try:
        reverse('djdt:render_panel')
    except NoReverseMatch:
        urlconf_module = import_module(settings.ROOT_URLCONF)
        urlconf_module.urlpatterns = [
                                         url(r'^__cpdebug__/', include(chrome_panel.urls)),
                                     ] + urlconf_module.urlpatterns
        clear_url_caches()


def patch_all():
    patch_middleware_classes()
