from django.core.cache import cache
from django.template.response import TemplateResponse


def index(request):
    cache.add('num', 1)
    cache.incr('num')
    num = cache.get('num')
    # return render(request, "charinfo/test.html")
    # return render(request, "charinfo/index.jinja", {'num': num})
    return TemplateResponse(request, "charinfo/index.jinja", {'num': num})


def index2(request):
    cache.add('num', 1)
    cache.incr('num')
    num = cache.get('num')
    # return render(request, "charinfo/test.html")
    return TemplateResponse(request, "charinfo/index2.jinja", {'num': num})


def index3(request):
    cache.add('num', 1)
    cache.incr('num')
    num = cache.get('num')
    return TemplateResponse(request, "charinfo/index3.jinja", {'num': num})
