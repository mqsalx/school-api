from rest_framework import generics

from school.models.registration import RegistrationModel
from school.serializers.registration_student import (
    ListRegistrationStudentSerializer,
)


class ListRegistrationStudentView(generics.ListAPIView):

    def get_queryset(self):
        queryset = RegistrationModel.objects.filter(
            student_id=self.kwargs["pk"]
        ).order_by("id")
        return queryset

    serializer_class = ListRegistrationStudentSerializer
