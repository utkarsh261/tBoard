from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import viewsets
from .serializers import InfoSerializer, DataSerializer
from .models import Info, Data


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer