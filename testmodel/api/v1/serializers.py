from rest_framework import serializers
from testmodel.models import Testmodel


class TestmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testmodel
        fields = "__all__"
