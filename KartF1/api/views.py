from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
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