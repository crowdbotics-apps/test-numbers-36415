from rest_framework import authentication
from three.models import Three
from .serializers import ThreeSerializer
from rest_framework import viewsets


class ThreeViewSet(viewsets.ModelViewSet):
    serializer_class = ThreeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Three.objects.all()
