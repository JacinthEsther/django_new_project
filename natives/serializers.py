from rest_framework import serializers

from natives.models import Native, Cohort


class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort
        fields = "__all__"


class NativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Native
        fields = ('id', 'email', 'first_name', 'last_name')
