from rest_framework import serializers

from school.models.registration import RegistrationModel


class ListRegistrationCourseSerializer(serializers.Serializer):

    student = serializers.ReadOnlyField(source="student.name")

    class Meta:
        model = RegistrationModel
        fields = ["student"]