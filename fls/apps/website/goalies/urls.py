from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.goalies, name='/goalies'),
    url(r'^tables$', views.tables, name='/goalies/tables'),
]