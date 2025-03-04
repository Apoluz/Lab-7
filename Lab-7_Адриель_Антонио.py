import requests

ISS_NOW_URL = "http://api.open-notify.org/iss-now.json"

# Координаты Санкт-Петербурга
широта = 59.9343
долгота = 30.3351


ответ_исс_сейчас = requests.get(ISS_NOW_URL)

if ответ_исс_сейчас.status_code == 200:
    данные_исс = ответ_исс_сейчас.json()
    исс_широта = данные_исс["iss_position"]["latitude"]
    исс_долгота = данные_исс["iss_position"]["longitude"]

    print(f"🚀 МКС в настоящее время находится в:")
    print(f"   🌍 Широта: {исс_широта}, Долгота: {исс_долгота}\n")
else:
    print("❌ Ошибка при получении текущего местоположения МКС:", ответ_исс_сейчас.status_code)





