from rest_framework.exceptions import ValidationError

from .constants import (
    GEOMETRY_TYPES,
    GEOMETRY_TYPES_ERROR,
    GEOMETRY_COORDINATES_ERROR,
    INPUT_DATA_FEATURE_FIELD_ERROR,
    INPUT_DATA_FEATURE_FIELD_TYPE_ERROR,
    INPUT_DATA_FEATURE_FIELD_TYPE_FIELD_ERROR,
    INPUT_DATA_FEATURE_FIELD_PROPERTIES_FIELD_ERROR,
    INPUT_DATA_FEATURE_FIELD_GEOMETRY_FIELD_ERROR,
    INPUT_DATA_TYPE_FIELD_ERROR,
    INPUT_DATA_TYPE_FIELD_VALUE_ERROR,

)


def validate_geo_input_dict(data_dict: dict) -> dict:
    """Валидатор для входных данных"""
    type = data_dict.get('type')
    if not type:
        raise ValidationError(INPUT_DATA_TYPE_FIELD_ERROR)
    if type != 'FeatureCollection':
        raise ValidationError(INPUT_DATA_TYPE_FIELD_VALUE_ERROR)
    features = data_dict.get('features')
    if not features:
        raise ValidationError(INPUT_DATA_FEATURE_FIELD_ERROR)
    if not isinstance(features, list):
        raise ValidationError(INPUT_DATA_FEATURE_FIELD_TYPE_ERROR)
    features = features[0]
    features_type = features.get('type')
    features_properties = features.get('properties')
    features_geometry = features.get('geometry')
    if not features_type:
        raise ValidationError(INPUT_DATA_FEATURE_FIELD_TYPE_FIELD_ERROR)
    if not features_properties:
        raise ValidationError(INPUT_DATA_FEATURE_FIELD_PROPERTIES_FIELD_ERROR)
    if not features_geometry:
        raise ValidationError(INPUT_DATA_FEATURE_FIELD_GEOMETRY_FIELD_ERROR)
    return data_dict


def validate_geometry(geometry: dict) -> dict:
    """Валидатор для геометрии."""
    type = geometry.get('type')
    coordinates = geometry.get('coordinates')
    if type not in GEOMETRY_TYPES:
        raise ValidationError(GEOMETRY_TYPES_ERROR)
    if not coordinates:
        raise ValidationError(GEOMETRY_COORDINATES_ERROR)
