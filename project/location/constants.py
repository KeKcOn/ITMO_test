MAX_LENGTH_COUNTRY = 256
MAX_LENGTH_CITY = 256

GEOMETRY_TYPES = ('Point', 'Polygon')

GEOMETRY_TYPES_ERROR = (
    f'Geometry types can only be: {",".join(GEOMETRY_TYPES)}.')
GEOMETRY_COORDINATES_ERROR = 'Must contain a field with coordinates.'
INPUT_DATA_TYPE_FIELD_ERROR = 'request must have a type field.'
INPUT_DATA_TYPE_FIELD_VALUE_ERROR = (
    'type field must have the value FeatureCollection.')
INPUT_DATA_FEATURE_FIELD_ERROR = 'request must have a features field.'
INPUT_DATA_FEATURE_FIELD_TYPE_ERROR = 'features field must be a list.'
INPUT_DATA_FEATURE_FIELD_TYPE_FIELD_ERROR = (
    'request must have a type field in features field.')
INPUT_DATA_FEATURE_FIELD_PROPERTIES_FIELD_ERROR = (
    'request must have a properties field in features field.')
INPUT_DATA_FEATURE_FIELD_GEOMETRY_FIELD_ERROR = (
    'request must have a geometry field in features field.')
