from rest_framework import serializers

from .models import Addition

class AdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addition
        fields = ('id','number1','number2','answer')


