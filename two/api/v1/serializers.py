from rest_framework import serializers
from two.models import Two


class TwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Two
        fields = "__all__"
