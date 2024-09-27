# 🛡️Throttling - School API

## 📜 Introduction

- Throttle was used in this project to limit the rate of requests a client can make to an API within a defined time period. This is useful for protecting the API from abuse or overuse, both by anonymous and authenticated users.

## 📝 In this project, as an example, we implement two custom Throttle classes:

- `RegistrationAnonRateThrottle`: Limits the number of daily logs for anonymous users.

- `RegistrationUserRateThrottle`: Limits the number of daily logs for authenticated users.

## ⚒️ How Does Throttling Work?

- Throttling is configured to ensure that a specific number of requests can be made within a given time frame. If a user exceeds this limit, a response with the status code 429 Too Many Requests is returned.

### 🔬 Configuration Example

- Below are examples of the two configured throttle classes

1. - **RegistrationAnonRateThrottle**

   This class inherits from `AnonRateThrottle` and sets a rate of 5 requests per day for anonymous users.

   ```python
   from rest_framework.throttling import AnonRateThrottle

   class RegistrationAnonRateThrottle(AnonRateThrottle):
       rate = "5/day"
   ```

   **Explanation**:

   - **Classe Base**: `AnonRateThrottle` is used for users who are not authenticated.
   - **Rate**: This value is set to "5/day", which means that an anonymous user can make up to 5 requests in a 24 hour period.

2. - **RegistrationUserRateThrottle**

   This class inherits from `UserRateThrottle` and sets a rate of 30 requests per day for authenticated users.

   ```python
   from rest_framework.throttling import UserRateThrottle

   class RegistrationUserRateThrottle(UserRateThrottle):
     rate = "30/day"
   ```

   **Explanation**:

   - **Classe Base**: `UserRateThrottle` is used for authenticated users.
   - **Rate**: The rate is set to "30/day", which means an authenticated user can make up to 30 requests in a 24-hour period.

## 👨🏽‍🏫 How to Use

- To apply these throttling rules, you need to add them to the view or set of views in your Django REST Framework

  ```python

  from rest_framework.views import APIView
  from .throttles import RegistrationAnonRateThrottle, RegistrationUserRateThrottle

  class UserView(APIView):
  throttle_classes = [RegistrationAnonRateThrottle, RegistrationUserRateThrottle]

  def post(self, request, *args, **kwargs):
      # registration logic here
      return Response({"message": "User registered successfully!"})
  ```

- Steps:

1. - Create the throttle classes in the **throttles.py** file.
2. - Add the throttle configuration to the view you want to limit the number of requests for, using the throttle_classes parameter.
3. - Define the view logic (in this case, the user registration logic).

## 🌐 Global Settings (Optional)
- If you prefer, you can configure these `throttle` classes globally, in the settings.py file, so that they apply to all views

    ```python
    REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
            "anon": "50/day",
            "user": "20/day"
        },
    }
    ```

## ✅ Conclusion
- Using throttling is essential to protect your API from abuse due to excessive requests.
When configured correctly, you can ensure that both anonymous and authenticated users follow the established limits, maintaining the health and security of your system.
