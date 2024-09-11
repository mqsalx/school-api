from rest_framework import generics

from school.models.registration import RegistrationModel
from school.serializers.registration_course import (
    ListRegistrationCourseSerializer,
)


class ListRegistrationCourseView(generics.ListAPIView):
    """
    View Description:
    - Lists enrollments by Course ID
    Params:
    - pk (int): the primary identifier of the object. Must be an integer.
    """

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return RegistrationModel.objects.none()
        queryset = RegistrationModel.objects.filter(
            course_id=self.kwargs["pk"]
        ).order_by("id")
        return queryset

    serializer_class = ListRegistrationCourseSerializer
