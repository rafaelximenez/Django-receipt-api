from django.conf.urls import url 
from rxmz import views 
 
urlpatterns = [ 
    url(r'^api/recibos$', views.index),
]