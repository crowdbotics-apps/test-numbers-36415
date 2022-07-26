from rest_framework import serializers
from four.models import Four


class FourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Four
        fields = "__all__"
