def generate_plan(city, weather):
  from openai import OpenAI

  if weather is None:
        print("❌ No se pudo generar un plan porque no hay información del clima.")
        return None
  descripcion = weather["weather"][0]["description"]
  temperatura = weather["main"]["temp"]
  resumen_clima = f"el clima está {descripcion} y la temperatura es de {temperatura}°C"


  client = OpenAI()

  completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "developer", 
          "content": "You are a travel expert and itinerary planner. \n"
          "Your task is to create a short and practical travel plan for a given city, \n"
          "based on the current weather conditions provided by the user. \n"
          "The plan should: \n"
          "- Be useful for someone spending a day in the city. \n"
          "- Adapt to the weather (e.g., avoid outdoor activities if it's raining). \n"
          "- Include 2 to 4 activity suggestions (like visiting landmarks, trying local food, museums, parks, etc.). \n"
          "- Be friendly, concise, and engaging. \n"
          "- Avoid generic statements or unnecessary details. \n"
          "Only return the travel plan. Do not include any explanations, headings, or extra text before or after the plan." },
      {"role": "user", 
          "content": f"Create a travel plan for {city} where {resumen_clima}."}
    ]
  )

  return completion.choices[0].message.content.strip()