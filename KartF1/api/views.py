from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import KartSerializer
from .models import Kart
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/karts/',
            'method': 'GET',
            'body' : None,
            'description' : 'Return array of karts'
        },
        {
            'Endpoint': '/karts/id',
            'method': 'GET',
            'body' : None,
            'description' : 'Return a kart'
        },
        {
            'Endpoint': '/karts/create',
            'method': 'POST',
            'body' : {'body': ""},
            'description' : 'Creates karts'
        },
        {
            'Endpoint': '/karts/id/update',
            'method': 'PUT',
            'body' : {'body': ""},
            'description' : 'Update a kart'
        },
        {
            'Endpoint': '/karts/id/delete',
            'method': 'DELETE',
            'body' : None,
            'description' : 'Delete a kart'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getKarts(request):
    karts = Kart.objects.all()
    serializer = KartSerializer(karts,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getKart(request, pk):
    kart = Kart.objects.get(id=pk)
    serializer = KartSerializer(kart,many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createKart(request):
    data = request.data

    kart = Kart.objects.create(
        body=data['body']
    )
    serializer = KartSerializer(kart, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateKart(request, pk):
    data = request.data

    kart = Kart.objects.get(id=pk)

    serializer = KartSerializer(kart, data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteKart(request, pk):
    kart = Kart.objects.get(id=pk)
    kart.delete()
    return Response('Borrado')