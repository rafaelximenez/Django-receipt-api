from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from rxmz.models import Recibos
from rxmz.serializers import RecibosSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    recibos = Recibos.objects.all()
        
    recibos_serializer = RecibosSerializer(recibos, many=True)
    return JsonResponse(recibos_serializer.data, safe=False)