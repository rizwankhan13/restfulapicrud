from rest_framework import serializers
from .models import Uzer

class UzerSerializer(serializers.ModelSerializer):
    class Meta:
        model =Uzer
        fields = '__all__'