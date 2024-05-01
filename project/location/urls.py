from django.urls import include, path
from rest_framework import routers

from .views import CapitalViewSet

router = routers.DefaultRouter()

router.register(
    'capital',
    CapitalViewSet,
    basename='capital',
)

urlpatterns = [
    path('', include(router.urls)),
]
