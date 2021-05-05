from rest_framework import serializers


def starts_with_d(value):
    if value[0].lower() != "d":
        raise serializers.ValidationError("name must start with d")
    return value