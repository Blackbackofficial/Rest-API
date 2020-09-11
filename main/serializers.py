from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.Serializer):
    person = serializers.CharField()
    # id = serializers.IntegerField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.person = validated_data.get('person', instance.person)
        instance.save()
        return instance
