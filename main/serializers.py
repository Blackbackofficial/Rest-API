from rest_framework import serializers
from main.models import Person


class PersonSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # name = serializers.CharField()
    # age = serializers.CharField()
    # address = serializers.CharField()
    # work = serializers.CharField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.address = validated_data.get('address', instance.address)
        instance.work = validated_data.get('work', instance.work)
        instance.save()
        return instance

    class Meta:
        model = Person
        fields = ('id', 'name', 'age', 'address', 'work')
