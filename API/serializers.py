from rest_framework import serializers
from .models import Book,Task,BTSMembers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = '__all__'


class BTSMembersSerializer(serializers.Serializer):
    id =serializers.IntegerField()
    MemberName = serializers.CharField(max_length=8)
    age = serializers.IntegerField()
    GoodThingAboutHim = serializers.CharField(max_length=100)

    def create(self,validate_data):
        return BTSMembers.objects.create(**validate_data)