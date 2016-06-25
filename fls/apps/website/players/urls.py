from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^skaters$', views.skaters, name='/skaters'),
    url(r'^goalies$', views.goalies, name='/goalies'),
]