from django.urls import include, path
from rest_framework import routers

from school.views.course import CourseView
from school.views.student import StudentView

router = routers.DefaultRouter()
router.register("students", StudentView, basename="student")
router.register("courses", CourseView, basename="course")

urlpatterns = [path("", include(router.urls))]
