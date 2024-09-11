from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from school.models.student import StudentModel
from school.serializers.student import StudentSerializer
from school.serializers.student_v2 import StudentSerializerV2


class StudentView(ModelViewSet):
    """
    A viewset for managing student data.
    Attributes:
        queryset (QuerySet): The queryset of all student objects.
        filter_backends (list): The list of filter backends used for filtering student objects.
        ordering_fields (list): The list of fields used for ordering student objects.
        search_fields (list): The list of fields used for searching student objects.
    Methods:
        get_serializer_class: Returns the appropriate serializer class based on the request version.
    """

    queryset = StudentModel.objects.all().order_by("id")
    # serializer_class = StudentSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["name"]
    search_fields = ["name", "cpf"]

    def get_serializer_class(self):
        if self.request.version == "v2":  # type: ignore
            return StudentSerializerV2
        return StudentSerializer
