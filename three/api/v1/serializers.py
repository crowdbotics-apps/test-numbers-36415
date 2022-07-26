from rest_framework import serializers
from three.models import Three


class ThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Three
        fields = "__all__"
