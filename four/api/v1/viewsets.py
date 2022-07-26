from rest_framework import authentication
from four.models import Four
from .serializers import FourSerializer
from rest_framework import viewsets


class FourViewSet(viewsets.ModelViewSet):
    serializer_class = FourSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Four.objects.all()
