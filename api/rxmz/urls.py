from django.conf.urls import url 
from rxmz import views 
 
urlpatterns = [ 
    url(r'^recibos$', views.index),
    url(r'^buscar/recibos/(?P<pk>[0-9]+)$', views.get),
    url(r'^criar/recibos', views.create),
    url(r'^alterar/recibos/(?P<pk>[0-9]+)$', views.change),
    url(r'^deletar/recibos/(?P<pk>[0-9]+)$', views.delete),
]