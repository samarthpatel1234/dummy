from django.shortcuts import render
from rest_framework.views import APIView
from dummayapp import serializer 
from django.http import HttpResponse

class DummyViewSet(APIView):
    def get(self, request):
        serializer_instance = serializer.serializer(data= request.data) 
        if serializer_instance.is_valid():
            return HttpResponse(serializer_instance.validated_data.get("data"))
    
        return HttpResponse("invalid")
        