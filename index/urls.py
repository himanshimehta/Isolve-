from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
url(r'^$', views.fun, name='fun' ),
url(r'^likepost/$', views.likePost, name='likepost'),
]
