def get_weather(coord):
    import requests
    from dotenv import load_dotenv
    import os

    if coord is None:
        print("❌ Coordenadas inválidas. No se puede obtener el clima.")
        return None  # ¡Faltaba este return!

    load_dotenv()
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")

    if not api_key:
        print("❌ No se encontró la API KEY de OpenWeather. Revisa tu archivo .env")
        return None

    url = f"https://api.openweathermap.org/data/2.5/weather?{coord}&appid={api_key}&units=metric&lang=es"

    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            print(f"❌ Error al obtener el clima: {respuesta.status_code} - {respuesta.json().get('message')}")
            return None
    except Exception as e:
        print(f"❌ Error de conexión al obtener el clima: {e}")
        return None
