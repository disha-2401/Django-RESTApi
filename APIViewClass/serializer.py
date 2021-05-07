from rest_framework import serializers
from .models import Student


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
