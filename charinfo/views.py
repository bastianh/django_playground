from time import sleep
from django.core.cache import cache
from django.template.response import TemplateResponse


def index(request):
    cache.add('num', 1)
    num = cache.incr('num')
    # return render(request, "charinfo/test.html")
    # return render(request, "charinfo/index.jinja", {'num': num})
    return TemplateResponse(request, "charinfo/index.jinja", {'num': num, 'page': 1})


def index2(request):
    cache.add('num', 1)
    num = cache.incr('num', 1)
    # return render(request, "charinfo/test.html")
    return TemplateResponse(request, "charinfo/index.jinja", {'num': num, 'page': 2})


def index3(request):
    cache.add('num', 1)
    num = cache.incr('num')
    return TemplateResponse(request, "charinfo/index.jinja", {'num': num, 'page': 3})
