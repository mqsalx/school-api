from rest_framework import serializers

from school.models.student import StudentModel
from school.serializers.validators import cpf_validate, name_alpha, phone_len


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

    def validate(self, data):

        if name_alpha(data["name"]):
            raise serializers.ValidationError(
                {"name": "Name must have only letters!"}
            )

        if cpf_validate(data["cpf"]):
            raise serializers.ValidationError(
                {"cpf": "CPF must have a valid value!"}
            )

        if phone_len(data["phone"]):
            raise serializers.ValidationError(
                {"phone": "Phone must have 11 digits! 99 99999-9999"}
            )

        return data
