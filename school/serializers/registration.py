from rest_framework import serializers

from school.models.registration import RegistrationModel


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationModel
        fields = "__all__"
