from rest_framework import serializers
from .models import *

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields ='__all__'