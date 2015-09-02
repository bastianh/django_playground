import threading
from chrome_panel.panel import DebugPanel


class ChromePanelMiddleware(object):
    debug_panel = {}

    def process_request(self, request):
        # Decide whether the toolbar is active for this request.
        # if not self.show_toolbar(request):
        #    print("dont show toolbar")
        #    return

        panel = DebugPanel(request)
        self.__class__.debug_panel[threading.current_thread().ident] = panel

    def process_response(self, request, response):
        panel = self.__class__.debug_panel.pop(threading.current_thread().ident, None)
        if not panel:
            return response

        response['X-CHROME-PANEL'] = "0.0.1"

        # TODO: add panel header
        return response
