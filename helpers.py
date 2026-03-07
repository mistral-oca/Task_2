import random
import string


def generate_user():
    rand = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

    return {
        "email": f"test_{rand}@yandex.ru",
        "password": "password",
        "name": f"user_{rand}"
    }