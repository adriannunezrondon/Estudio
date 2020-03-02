from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login


urlpatterns = [
    # Examples:
    # url(r'^$', 'Estudio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mascota/', include('AppEstudio.urls', namespace='mascota')),
    url(r'^usuario/', include('usuario.urls', namespace='usuario')),

    # Login
    url(r'^accounts/login/', login, {'template_name': 'index.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
]
