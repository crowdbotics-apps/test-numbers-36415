from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ThreeViewSet

router = DefaultRouter()
router.register("three", ThreeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
