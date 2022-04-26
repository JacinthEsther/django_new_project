from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class NativeViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=['get'])
    def call_fola(self, request):
        return Response({})


class CohortViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=['get'])
    def show_name(self, request):
        return Response({"name": "Esther"})
