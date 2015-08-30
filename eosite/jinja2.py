from jinja2 import Environment as Jinja2Environment


class ConfiguredJinja2Environment(Jinja2Environment):
    def __init__(self, *a, **kw):
        Jinja2Environment.__init__(self, *a, **kw)
        from django_assets.env import get_env
        self.assets_environment = get_env()
