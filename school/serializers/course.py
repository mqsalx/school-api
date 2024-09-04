from rest_framework import serializers

from school.models.course import CourseModel


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = "__all__"
