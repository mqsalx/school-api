from django.db import models


class CourseModel(models.Model):

    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    )

    code = models.CharField(max_length=10)
    description = models.EmailField(max_length=100, blank=False)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.code
