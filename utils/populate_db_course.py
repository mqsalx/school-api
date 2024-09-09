import os
import random
import sys

import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()


data = [
    ("CPOO1", "Curso de Python Orientação à Objetos 01"),
    ("CPOO2", "Curso de Python Orientação à Objetos 02"),
    ("CPOO3", "Curso de Python Orientação à Objetos 03"),
    ("CDJ01", "Curso de Django 01"),
    ("CDJ02", "Curso de Django 02"),
    ("CDJ03", "Curso de Django 03"),
    ("CDJ04", "Curso de Django 04"),
    ("CDJ05", "Curso de Django 05"),
    ("CDJRF01", "Curso de Django REST Framework 01"),
    ("CDJRF02", "Curso de Django REST Framework 02"),
    ("CDJRF03", "Curso de Django REST Framework 03"),
    ("CDJRF04", "Curso de Django REST Framework 04"),
]

_level = ["B", "I", "A"]


def create_course():

    from school.models.course import CourseModel

    for code, description in data:
        level = random.choice(_level)
        CourseModel.objects.create(
            code=code, description=description, level=level
        )


create_course()
