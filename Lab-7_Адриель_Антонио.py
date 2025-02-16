import requests
from requests.auth import HTTPBasicAuth

# Credenciales
USERNAME = "itmouniversity_arrietaalvarado_adryelantonio"
PASSWORD = "Z8Hw1gL8Fq"

# URL con la fecha y coordenadas de San Petersburgo
URL = "https://api.meteomatics.com/2025-02-16T12:00:00Z/t_2m:C/59.9343,30.3351/json"

# Hacer la solicitud con autenticación
response = requests.get(URL, auth=HTTPBasicAuth(USERNAME, PASSWORD))

# Verificar respuesta
if response.status_code == 200:
    data = response.json()
    
    # Ajuste correcto para acceder a la temperatura
    temp_value = data["data"][0]["coordinates"][0]["dates"][0]["value"]
    
    print(f"🌍 Город: San Petersburgo")
    print(f"🌡️ Температура: {temp_value}°C")
else:
    print("❌ Error:", response.status_code, response.text)

