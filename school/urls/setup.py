from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from school.views.course import CourseView
from school.views.registration import RegistrationView
from school.views.registration_course import ListRegistrationCourseView
from school.views.registration_student import ListRegistrationStudentView
from school.views.student import StudentView

router = routers.DefaultRouter()
router.register("students", StudentView, basename="students")
router.register("courses", CourseView, basename="courses")
router.register("registrations", RegistrationView, basename="registrations")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("courses/<int:pk>/registrations/", ListRegistrationCourseView.as_view()),
    path("students/<int:pk>/registrations/", ListRegistrationStudentView.as_view()),
]
