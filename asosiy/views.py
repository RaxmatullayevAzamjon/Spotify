from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


class QoshiqAPI(APIView):
    def get(self, request):
        qoshiq = Qoshiq.objects.all()
        serializer = QoshiqSerializer(qoshiq, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=QoshiqSerializer)
    def post(self, request):
        qoshiq = request.data
        serializer = QoshiqSerializer(data=qoshiq)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @swagger_auto_schema(request_body=QoshiqSerializer)
    def update(self, request, son):
        data = request.data
        qoshiq = Qoshiq.objects.get(id=son)
        serializer = QoshiqSerializer(qoshiq, data=data)
        if serializer.is_valid():
            qoshiq.update(
                nom =serializer.validated_data.get("nom")
            )
            return Response(serializer.data)
        return Response(serializer.errors)



class AlbomModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomPOSTSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nom", "janr", "albom"]
    ordring_fields = ["davomiylik"]





