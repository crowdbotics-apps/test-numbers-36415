from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TestmodelViewSet

router = DefaultRouter()
router.register("testmodel", TestmodelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
