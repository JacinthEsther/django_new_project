from rest_framework import serializers

from portfolio.models import Project


class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
