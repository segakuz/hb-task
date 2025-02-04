import random
import string


def generate_email(length: int = 8, domain: str = 'test.test'):
    """
    Generates random email with specified domain

    :param length: length of email
    :param domain: domain
    """

    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    return f"{random_string}@{domain}"

def generate_name():
    """
    Generates random test name
    """

    first_name_letter = ''.join(random.choices(string.ascii_uppercase))
    ending_name_letters = ''.join(random.choices(string.ascii_lowercase, k=2))
    last_name = ''.join(random.choices(string.ascii_uppercase, k=6))

    return f"{first_name_letter}test{ending_name_letters} {last_name.capitalize()}"

def generate_phone_number():
    """
    Generates random test phone number
    """

    return '555555' + ''.join(random.choices(string.digits, k=4))
