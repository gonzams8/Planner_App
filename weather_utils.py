def get_weather(coord):
    import requests
    from dotenv import load_dotenv
    import os

    if coord is None:
        print("❌ Coordenadas inválidas. No se puede obtener el clima")

    load_dotenv()
    api_key = os.getenv("WEATHER_API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/weather?{coord}&appid={api_key}&units=metric&lang=es"

    respuesta = requests.get(url)

    # Verificar el estado
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
