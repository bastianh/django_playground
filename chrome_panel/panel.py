from collections import OrderedDict

from chrome_panel import settings as cp_settings


class DebugPanel(object):
    def __init__(self, request):
        self.request = request
        # self.config = cp_settings.CONFIG.copy()
        self._panels = OrderedDict()
        # for panel_class in self.get_panel_classes():
        #    panel_instance = panel_class(self)
        #    self._panels[panel_instance.panel_id] = panel_instance
        self.stats = {}
        self.store_id = None
