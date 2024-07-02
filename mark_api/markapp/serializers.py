from rest_framework import serializers
from .models import *

class Marksheetserializer(serializers.ModelSerializer):
    class Meta:
        model=Marksheet
        fields=('id','subject','mark','performance')