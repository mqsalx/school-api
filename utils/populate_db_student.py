import os
import random
import sys

import django
from faker import Faker
from validate_docbr import CPF

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()


def create_person(quantity):
    from school.models.student import StudentModel

    fake = Faker("pt_BR")
    Faker.seed(10)
    for _ in range(quantity):
        cpf = CPF()
        name = fake.name()
        email = "{}@{}".format(name.lower(), fake.free_email_domain())
        email = email.replace(" ", "")
        cpf = cpf.generate()
        b_day = fake.date_of_birth(minimum_age=18, maximum_age=30)
        phone = "{} 9{}-{}".format(
            random.randrange(10, 89),
            random.randrange(4000, 9999),
            random.randrange(4000, 9999),
        )
        p = StudentModel(
            name=name,
            email=email,
            cpf=cpf,
            b_day=b_day,
            phone=phone,
        )
        p.save()


create_person(50)
