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

@api_view(['GET'])
def get(request, pk):
    recibos = Recibos.objects.get(pk=pk)
    recibos_serializer = RecibosSerializer(recibos) 
    return JsonResponse(recibos_serializer.data)

@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        request_body = JSONParser().parse(request)
        recibos_serializer = RecibosSerializer(data=request_body) 
        if recibos_serializer.is_valid():
            recibos_serializer.save()
            return JsonResponse(recibos_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return "Método não suportado", 405

@api_view(['PUT'])
def change(request, pk):
    if request.method == 'PUT':
        recibo = Recibos.objects.get(pk=pk)
        request_body = JSONParser().parse(request)
        recibos_serializer = RecibosSerializer(recibo, data=request_body)
        if recibos_serializer.is_valid():
            recibos_serializer.save()
            return JsonResponse(recibos_serializer.data)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return "Método não suportado", 405

@api_view(['DELETE'])
def delete(request, pk):
    if request.method == 'DELETE':
        recibo = Recibos.objects.get(pk=pk)
        recibo.delete()
        return JsonResponse({'message': 'O recibo foi excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
    return "Método não suportado", 405