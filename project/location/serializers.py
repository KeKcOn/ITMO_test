from rest_framework import serializers

from .models import Capital


class CapitalOutputSerializer(serializers.ModelSerializer):
    properties = serializers.SerializerMethodField()

    class Meta:
        model = Capital
        fields = ('properties', 'geometry', 'id',)

    def get_properties(self, obj):
        return {
            'country': obj.country,
            'city': obj.city,
        }

    def to_representation(self, instance):
        instance = super().to_representation(instance)
        instance = {
            'type': 'Feature',
            'properties': instance.get('properties'),
            'geometry': instance.get('geometry'),
            'id': instance.get('id'),
        }
        return instance


class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = ('country', 'city', 'geometry',)

    def to_representation(self, instance):
        return CapitalOutputSerializer(instance).data
