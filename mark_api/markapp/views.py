from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class sublist(generics.ListCreateAPIView):
    queryset=Marksheet.objects.all()
    serializer_class=Marksheetserializer

class subdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Marksheet
    serializer_class=Marksheetserializer    