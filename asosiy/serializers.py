from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class QoshiqchiSerializer(serializers.Serializer):
    ism = serializers.CharField()
    tugilgan_yil = serializers.DateField()
    davlat = serializers.CharField()



class AlbomSerializer(serializers.ModelSerializer):
    qoshiqchi = QoshiqchiSerializer()
    class Meta:
        model = Albom
        fields = "__all__"

class AlbomPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = "__all__"



class QoshiqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = "__all__"








