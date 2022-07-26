from rest_framework import authentication
from two.models import Two
from .serializers import TwoSerializer
from rest_framework import viewsets


class TwoViewSet(viewsets.ModelViewSet):
    serializer_class = TwoSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Two.objects.all()
