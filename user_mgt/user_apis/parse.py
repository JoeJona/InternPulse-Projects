from rest_framework import serializers
from .models import User


class UserJsonParse(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']

