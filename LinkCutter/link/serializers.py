from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    """Сериализатор модели Link"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    success_url = serializers.ReadOnlyField()

    class Meta:
        model = Link
        fields = '__all__'