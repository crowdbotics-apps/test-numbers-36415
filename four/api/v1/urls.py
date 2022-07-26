from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FourViewSet

router = DefaultRouter()
router.register("four", FourViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
