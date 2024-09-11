from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from school.models.course import CourseModel
from school.serializers.course import CourseSerializer


class CourseView(ModelViewSet):
    """
    A viewset for managing courses.
    Attributes:
        queryset (QuerySet): The queryset of CourseModel objects.
        serializer_class (Serializer): The serializer class for CourseModel objects.
    """

    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = CourseModel.objects.all().order_by("id")
    serializer_class = CourseSerializer
