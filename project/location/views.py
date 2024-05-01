from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Capital
from .serializers import CapitalSerializer
from .validators import validate_geo_input_dict


class CapitalViewSet(ModelViewSet):
    serializer_class = CapitalSerializer
    queryset = Capital.objects.all()

    def _prepare_response_list_data(self, data):
        return {
            'type': 'FeatureCollection',
            'features': data
        }

    def _prepare_response_data(self, data):
        return {
            'type': 'FeatureCollection',
            'features': [data]
        }

    def _get_capital_data(self, data):
        features = data.get('features')[0]
        prop = features.get('properties')
        return {
            'country': prop.get('country'),
            'city': prop.get('city'),
            'geometry': features.get('geometry')
        }

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(self._prepare_response_data(serializer.data))

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(self._prepare_response_list_data(serializer.data))

    def create(self, request, *args, **kwargs):
        validated_data = validate_geo_input_dict(request.data)
        data = self._get_capital_data(validated_data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(self._prepare_response_data(serializer.data),
                        status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        validated_data = validate_geo_input_dict(request.data)
        data = self._get_capital_data(validated_data)
        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(self._prepare_response_data(serializer.data))
