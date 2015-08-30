from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^2$', views.index2, name='index2'),
    url(r'^3$', views.index3, name='index3'),

]