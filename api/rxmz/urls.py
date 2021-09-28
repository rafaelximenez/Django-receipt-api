from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rxmz import views 
 
urlpatterns = [ 
    #path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    url(r'^recibos$', views.index),
    url(r'^buscar/recibos/(?P<pk>[0-9]+)$', views.get),
    url(r'^criar/recibos', views.create),
    url(r'^alterar/recibos/(?P<pk>[0-9]+)$', views.change),
    url(r'^deletar/recibos/(?P<pk>[0-9]+)$', views.delete),
]