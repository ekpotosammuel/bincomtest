from rest_framework import serializers
from .models import Election, Type

class ElectionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Election
    fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Type
    fields = '__all__'