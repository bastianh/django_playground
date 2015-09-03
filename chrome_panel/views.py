from django.http import HttpResponse
from django.utils.html import escape
from django.utils.translation import ugettext as _

# Create your views here.
from chrome_panel.panel import DebugPanel


def render_panel(request):
    """Render the contents of a panel"""
    toolbar = DebugPanel.fetch(request.GET['store_id'])
    if toolbar is None:
        content = _("Data for this panel isn't available anymore. "
                    "Please reload the page and retry.")
        content = "<p>%s</p>" % escape(content)
    else:
        panel = toolbar.get_panel_by_id(request.GET['panel_id'])
        content = panel.content
    return HttpResponse(content)
