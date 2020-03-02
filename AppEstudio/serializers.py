__author__ = 'adrian'

from rest_framework.serializers import ModelSerializer
from AppEstudio.models import  Mascota

class MascotaSerializer(ModelSerializer):
    class Meta:
        model = Mascota
        fields = ('nombre', 'sexo', 'edad_aproximada', 'fecha_rescate', 'persona', 'vacuna')
