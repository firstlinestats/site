from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.skaters, name='/skaters'),
    url(r'^tables$', views.tables, name='/skaters/tables'),
]