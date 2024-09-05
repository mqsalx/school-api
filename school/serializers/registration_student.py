from rest_framework import serializers

from school.models.registration import RegistrationModel


class ListRegistrationStudentSerializer(serializers.Serializer):

    course = serializers.ReadOnlyField(source="course.description")
    period = serializers.SerializerMethodField()

    class Meta:
        model = RegistrationModel
        fields = ["course", "period"]

    def get_period(self, obj):
        return obj.get_period_display()