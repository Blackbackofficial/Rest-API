from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    person = serializers.CharField()
    id = serializers.IntegerField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.person = validated_data.get('person', instance.person)
        instance.save()
        return instance
