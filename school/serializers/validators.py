import re

from validate_docbr import CPF


def name_alpha(name_value):
    return not name_value.replace(" ", "").isalpha()


def cpf_validate(cpf_value):
    cpf = CPF()
    cpf_is_valid = cpf.validate(cpf_value)
    return not cpf_is_valid


def phone_len(phone_value):
    # 86 99999-9999
    model = "[0-9]{2} [0-9]{5}-[0-9]{4}"
    response = re.findall(model, phone_value)
    return not response
