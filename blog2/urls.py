from django.conf.urls import url
from blog2 import views

urlpatterns = [
    url(r'^$', views.index),
]