from rest_framework import generics

from school.models.registration import RegistrationModel
from school.serializers.registration_course import ListRegistrationCourseSerializer


class ListRegistrationCourseView(generics.ListAPIView):

    def get_queryset(self):
        queryset = RegistrationModel.objects.filter(course_id=self.kwargs["pk"])
        return queryset
    serializer_class = ListRegistrationCourseSerializer