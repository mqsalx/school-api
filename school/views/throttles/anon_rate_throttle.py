from rest_framework.throttling import AnonRateThrottle


class RegistrationAnonRateThrottle(AnonRateThrottle):
    rate = "5/day"
