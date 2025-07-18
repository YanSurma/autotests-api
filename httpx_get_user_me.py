import httpx

import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {
    "email": "yansurma@example.com",
    "password": "q1w2e3r4"
}
# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Формируем payload для обновления токена
refresh_payload = {
    "refreshToken": login_response_data["token"]["refreshToken"]
}
# Выполняем запрос на обновление токена
refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

# Выводим и сохраняем токен для дальнейшей работы
print("accessToken:", refresh_response_data["token"]["accessToken"])
access_token = refresh_response_data["token"]["accessToken"]

# Выполняем запрос get /users/me
headers = {"Authorization":  f"Bearer {access_token}"}
get_user_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
get_user_me_response_data = get_user_me_response.json()
print(get_user_me_response_data)  # Заголовки включены в ответ
print(get_user_me_response.status_code)