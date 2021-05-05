from rest_framework import serializers
from .models import Student
from . import validatorFunctions


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seats are full")
        return value

    def validate(self, value):
        name = value.get('name')
        if name.lower() != "disha":
            raise serializers.ValidationError("name must be disha")
        return value

# class StudentSerialiser(serializers.Serializer):
#     name = serializers.CharField(max_length=30,validators=[validatorFunctions.starts_with_d])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=30)
#
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         print("pehle ye ",instance.name," tha")
#         instance.name= validated_data.get('name',instance.name)
#         print("ab ye ",instance.name," hai 😁")
#         print("pehle ye ", instance.roll, " tha")
#         instance.roll= validated_data.get('roll',instance.roll)
#         print("ab ye ", instance.roll, " hai 😁")
#         print("pehle ye ", instance.city, " tha")
#         instance.city=validated_data.get('city',instance.city)
#         print("ab ye ", instance.city, " hai 😁")
#         instance.save()
#         return instance
#
#     def validate_roll(self,value):
#         if value >= 200:
#             raise serializers.ValidationError("Seats are full")
#         return value

# def validate(self,value):
#     name=value.get('name')
#     if name.lower() != "disha":
#         raise serializers.ValidationError("name must be disha")
#     return value
