from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^searchbycity$', views.searchbycity),
    url(r'^searchbyname$', views.searchbyname),
    #url(r'^senddata$', views.senddata),
]
