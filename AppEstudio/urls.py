from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from AppEstudio.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList,\
     MascotaCreate, MascotaUpdate, MascotaDelete, PersonaList, PersonaCreate, MascotaAPI


urlpatterns = [

    # Url Mascota CRUD

    url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    url(r'^listar$', login_required(MascotaList.as_view()), name='mascota_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name='mascota_edit'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_delete'),

    # Url Persona CRUD

    url(r'^persona/listar$', PersonaList.as_view(), name='persona_listar'),
    url(r'^persona/nuevo', PersonaCreate.as_view(), name='persona_crear'),

    #URL SERVICIOS MASCOTAS
    url(r'^api', MascotaAPI.as_view(), name='api'),

]
