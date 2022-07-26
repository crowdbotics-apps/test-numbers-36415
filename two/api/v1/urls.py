from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TwoViewSet

router = DefaultRouter()
router.register("two", TwoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
