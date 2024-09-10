from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from school.models.student import StudentModel
from school.serializers.student import StudentSerializer
from school.serializers.student_v2 import StudentSerializerV2


class StudentView(ModelViewSet):

    queryset = StudentModel.objects.all()
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
