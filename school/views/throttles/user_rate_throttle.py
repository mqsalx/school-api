from rest_framework.throttling import UserRateThrottle


class RegistrationUserRateThrottle(UserRateThrottle):
    rate = "30/day"
