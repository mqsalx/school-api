from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from school.views.course import CourseView
from school.views.documentation import schema_view
from school.views.registration import RegistrationView
from school.views.registration_course import ListRegistrationCourseView
from school.views.registration_student import ListRegistrationStudentView
from school.views.student import StudentView

router = routers.DefaultRouter()
router.register("students", StudentView, basename="students")
router.register("courses", CourseView, basename="courses")
router.register("registrations", RegistrationView, basename="registrations")

urlpatterns = [
    re_path(
        r"^favicon\.ico$",
        RedirectView.as_view(url="/static/favicon.ico"),
    ),
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path(
        "courses/<int:pk>/registrations/", ListRegistrationCourseView.as_view()
    ),
    path(
        "students/<int:pk>/registrations/",
        ListRegistrationStudentView.as_view(),
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
