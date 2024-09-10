from rest_framework.viewsets import ModelViewSet

from school.models.registration import RegistrationModel
from school.serializers.registration import RegistrationSerializer
from school.views.throttles.anon_rate_throttle import (
    RegistrationAnonRateThrottle,
)
from school.views.throttles.user_rate_throttle import (
    RegistrationUserRateThrottle,
)


class RegistrationView(ModelViewSet):

    queryset = RegistrationModel.objects.all().order_by("id")
    serializer_class = RegistrationSerializer
    throttle_classes = [
        RegistrationUserRateThrottle,
        RegistrationAnonRateThrottle,
    ]
