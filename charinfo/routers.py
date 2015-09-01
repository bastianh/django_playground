from datetime import datetime

from swampdragon import route_handler
from swampdragon.route_handler import BaseRouter


class FooRouter(BaseRouter):
    route_name = 'foo'
    valid_verbs = ['get_date', 'get_error']

    def get_date(self, **kwargs):
        self.send({'current_date': str(datetime.now()), "kwargs": kwargs})

    def get_error(self, **kwargs):
        self.send_error({'name': 'the name is required'})


route_handler.register(FooRouter)
