from rest_framework import serializers

from school.models.student import StudentModel


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = [
            "id",
            "name",
            "email",
            "cpf",
            "b_day",
            "phone",
        ]
