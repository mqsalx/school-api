from rest_framework.viewsets import ModelViewSet

from school.models.student import StudentModel
from school.serializers.student import StudentSerializer


class StudentView(ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
