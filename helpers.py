import random
import string
from datetime import datetime, timedelta


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = None
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_random_number(length):
    digits = "0123456789"
    random_number = None
    random_number = int(''.join(random.choice(digits) for i in range(length)))
    return random_number


def generate_random_phone_number():
    digits = "0123456789"
    random_phone_number = None
    random_phone_number = '8'.join(random.choice(digits) for i in range(10))
    return random_phone_number


def generate_random_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2030, 1, 1)
    random_date = None
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date
