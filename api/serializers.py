import uuid

from rest_framework import serializers

from .models import UUIDData


class UUIDDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UUIDData
        fields = "__all__"

    def create(self, validated_data):
        test_data = UUIDData.objects.create(**validated_data)
        return test_data

    def to_representation(self, instance):
        """Convert response to desired representation. i.e Key will be a timestamp and value will be UUID."""
        result = super().to_representation(instance)
        timestamp = result["created_date"]
        result[timestamp] = uuid.UUID(result["generated_uuid"]).hex
        del result["id"]
        del result["created_date"]
        del result["generated_uuid"]

        return result
