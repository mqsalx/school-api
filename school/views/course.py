from rest_framework.viewsets import ModelViewSet

from school.models.course import CourseModel
from school.serializers.course import CourseSerializer


class CourseView(ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
