BASE_URL = "https://stellarburgers.education-services.ru"

REGISTER_URL = BASE_URL + "/api/auth/register"
LOGIN_URL = BASE_URL + "/api/auth/login"
DELETE_USER_URL = BASE_URL + "/api/auth/user"
UPDATE_USER_URL = BASE_URL + "/api/auth/user"

ORDERS_URL = BASE_URL + "/api/orders"
INGREDIENTS_URL = BASE_URL + "/api/ingredients"

USER_WITHOUT_NAME = {
    "email": "test@yandex.ru",
    "password": "password"
}

ERROR_REQUIRED_FIELDS = "Email, password and name are required fields"
ERROR_USER_EXISTS = "User already exists"