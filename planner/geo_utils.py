def get_coordinates(city):
  from openai import OpenAI

  client = OpenAI()

  completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "developer", 
          "content": "You are a geography expert. Your task is to return the geographical coordinates (latitude and longitude) of a given city provided by the user. \n"
          "Always return the result in the following format: lat={lat}&lon={lon} \n"
          "Do not include any explanation, description, or additional text. Only return the formatted coordinates. \n"
          "If the city is not found, respond with: lat=NA&lon=NA" },
      {"role": "user", 
          "content": f"Give me the coordinates for {city}"}
    ]
  )

  result = completion.choices[0].message.content.strip()

  if "lat=NA" in result or "lon=NA" in result:
      print("⚠️ Ciudad no encontrada. Verifica el nombre e intenta nuevamente.")
      return None

  # Parseo seguro
  try:
      lat, lon = result.replace("lat=", "").replace("lon=", "").split("&")
      return f"lat={lat}&lon={lon}"
  except Exception as e:
      print(f"❌ Error al parsear coordenadas: {e}")
      return None