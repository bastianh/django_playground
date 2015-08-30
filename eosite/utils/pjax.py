from django.conf import settings
from pip import logger

PJAX_BASE_TEMPLATE = getattr(settings, 'PJAX_BASE_TEMPLATE', 'base_pjax.jinja')
BASE_TEMPLATE = getattr(settings, 'BASE_TEMPLATE', 'base.jinja')
PJAX_VERSION = getattr(settings, 'PJAX_VERSION', None)


class PjaxMiddleware(object):
    def process_request(self, request):
        print("process_request", request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("process_view", request, view_func, view_args, view_kwargs)

    def process_template_response(self, request, response):
        print("process_template_response", request, response)
        if request.META.get('HTTP_X_PJAX', False):
            logger.debug('pjax response')
            response.context_data['template_base'] = PJAX_BASE_TEMPLATE
            # fix redirect problem
            url = '%s?%s' % (request.path, request.META['QUERY_STRING'])
            response['X-PJAX-URL'] = url
            # set version
            if PJAX_VERSION:
                response['X-PJAX-Version'] = PJAX_VERSION
        else:
            logger.debug('full response')
            response.context_data['template_base'] = BASE_TEMPLATE
        return response

    def process_response(self, request, response):
        print("process_response(request, response)", request, response)
        return response
