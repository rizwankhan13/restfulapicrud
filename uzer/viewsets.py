from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Uzer.objects.all()
    serializer_class = serializers.UzerSerializer