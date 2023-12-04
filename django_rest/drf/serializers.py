from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *


class WonderSerializerCustom(serializers.Serializer):
    CHOICES = ['Exists', 'Destroyed']
    title = serializers.CharField(max_length=25)
    creator = serializers.CharField(max_length=25)
    created = serializers.DateField()
    place = serializers.CharField(max_length=50)
    current_status = serializers.ChoiceField(choices=CHOICES)

    def create(self, validated_data):
        return Wonder.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.creator = validated_data.get('creator', instance.creator)
        instance.created = validated_data.get('created', instance.created)
        instance.place = validated_data.get('place', instance.place)
        instance.current_status = validated_data.get('current_status', instance.current_status)
        instance.save()
        return instance
