from geo_utils import get_coordinates
from weather_utils import get_weather
from plan_generator import generate_plan
from voice_utils import text_to_speech

def main():
    city = input("🌍 Ingresa una ciudad: ")

    coor = get_coordinates(city)
    if coor is None:
        return

    weather = get_weather(coor)
    if weather is None:
        return

    plan = generate_plan(city, weather)
    if plan is None:
        return

    audio_path = text_to_speech(plan)
    if audio_path:
        print(f"🎧 Escucha tu plan de viaje en: {audio_path}")

# Ejecutar el programa
if __name__ == "__main__":
    main()