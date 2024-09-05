from django.db import models

from school.models.course import CourseModel
from school.models.student import StudentModel


class RegistrationModel(models.Model):

    PERIOD = (
        ("M", "Morning"),
        ("A", "Afternoon"),
        ("N", "Night"),
    )

    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    period = models.CharField(
        max_length=1, choices=PERIOD, blank=False, null=False, default="M"
    )

    def __str__(self):
        return f"{self.student} - {self.course}"
