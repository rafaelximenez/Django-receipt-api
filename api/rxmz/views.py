
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import status

from rxmz.serializers import RecibosSerializer
from rxmz.models import Recibos

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    recibos = Recibos.objects.all()
    recibos_serializer = RecibosSerializer(recibos, many=True)
    return JsonResponse(recibos_serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request, pk):
    try:
        recibos = Recibos.objects.get(pk=pk)
    except:
        return JsonResponse({'message': 'Erro ao buscar recibo!'}, status=status.HTTP_400_BAD_REQUEST)

    recibos_serializer = RecibosSerializer(recibos)      
    return JsonResponse(recibos_serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def delete(request, pk):
    if request.method == 'DELETE':
        recibo = Recibos.objects.get(pk=pk)
        recibo.delete()
        return JsonResponse({'message': 'O recibo foi excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
    return "Método não suportado", 405