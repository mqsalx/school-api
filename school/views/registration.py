
from rest_framework.viewsets import ModelViewSet

from school.models.registration import RegistrationModel
from school.serializers.registration import RegistrationSerializer


class RegistrationView(ModelViewSet):

    queryset = RegistrationModel.objects.all()
    serializer_class = RegistrationSerializer
