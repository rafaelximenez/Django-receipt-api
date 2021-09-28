from rest_framework import serializers 
from rxmz.models import Recibos
 
 
class RecibosSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Recibos
        fields = ('id',
                  'titulo',
                  'descricao',
                  'data')