from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    """Сериализатор модели Link"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    success_url = serializers.ReadOnlyField()

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta:
        model = Link
        fields = '__all__'