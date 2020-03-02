from django.conf.urls import include, url
from django.contrib import admin
from usuario.views import RegistroUsurio

urlpatterns = [
    # Examples:
    url(r'^registrar', RegistroUsurio.as_view(), name='registrar'),


]
