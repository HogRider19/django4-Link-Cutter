from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    """Сериализатор модели Link"""
    class Meta:
        model = Link
        fields = '__all__'