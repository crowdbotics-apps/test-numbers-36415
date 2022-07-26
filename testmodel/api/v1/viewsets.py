from rest_framework import authentication
from testmodel.models import Testmodel
from .serializers import TestmodelSerializer
from rest_framework import viewsets


class TestmodelViewSet(viewsets.ModelViewSet):
    serializer_class = TestmodelSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Testmodel.objects.all()
