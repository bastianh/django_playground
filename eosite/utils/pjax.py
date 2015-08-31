from django.conf import settings
from pip import logger

PJAX_BASE_TEMPLATE = getattr(settings, 'PJAX_BASE_TEMPLATE', 'base_pjax.jinja')
BASE_TEMPLATE = getattr(settings, 'BASE_TEMPLATE', 'base.jinja')
PJAX_VERSION = getattr(settings, 'PJAX_VERSION', None)


class PjaxMiddleware(object):
    def process_template_response(self, request, response):
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
