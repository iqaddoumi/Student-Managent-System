from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class MyAPIView(APIView):
    def get(self, request):
        print('MyAPIView GET request received')
        data = {
            'message': 'Hello, world!'
        }
        return Response(data)
