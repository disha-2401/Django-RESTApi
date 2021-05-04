from rest_framework import serializers
from .models import Student


class StudentSerialiser(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print("pehle ye ",instance.name," tha")
        instance.name= validated_data.get('name',instance.name)
        print("ab ye ",instance.name," hai")
        print("pehle ye ", instance.roll, " tha")
        instance.roll= validated_data.get('roll',instance.roll)
        print("ab ye ", instance.roll, " hai")
        print("pehle ye ", instance.city, " tha")
        instance.city=validated_data.get('city',instance.city)
        print("ab ye ", instance.city, " hai")
        instance.save()
        return instance