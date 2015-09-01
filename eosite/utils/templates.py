from django.conf import settings
from markupsafe import Markup


def swampdragon_settings():
    root_url = getattr(settings, 'DRAGON_URL') or 'http://localhost:9999/'
    if not root_url.endswith('/'):
        root_url += '/'
    return Markup('<script type="text/javascript" src="{}settings.js"></script>'.format(root_url))
