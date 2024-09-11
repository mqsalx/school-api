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
    """
    A view for handling registration related operations.
    Attributes:
        http_method_names (list): A list of allowed HTTP methods for this view.
        queryset (QuerySet): The queryset of RegistrationModel objects.
        serializer_class (Serializer): The serializer class for RegistrationModel.
        throttle_classes (list): A list of throttle classes for rate limiting.
    """

    http_method_names = ["get", "post"]
    queryset = RegistrationModel.objects.all().order_by("id")
    serializer_class = RegistrationSerializer
    throttle_classes = [
        RegistrationUserRateThrottle,
        RegistrationAnonRateThrottle,
    ]
