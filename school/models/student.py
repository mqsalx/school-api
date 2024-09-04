from django.db import models


class StudentModel(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11)
    b_day = models.DateField()
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name
