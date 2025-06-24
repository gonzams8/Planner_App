# 🌦️ VoiceWeather Planner
**A Python app that combines OpenWeatherMap, OpenAI, and ElevenLabs to suggest weather-based plans for any city — and reads them out loud!**
Perfect as a daily assistant or creative side project.

**The app is built in Spanish, showcasing my ability to develop multilingual solutions.**

## 🧠 What does this app do?
1. Gets the current weather of any city using OpenWeatherMap.
2. Uses OpenAI to generate personalized plans based on real-time weather conditions.
3. Converts the generated plan into natural speech using ElevenLabs' voice AI.

## 🛠️ Tech Stack

- **Python 3**
- **OpenWeatherMap API** – for real-time weather data.
- **OpenAI API** – to generate creative and weather-appropriate suggestions.
- **ElevenLabs API** – for realistic text-to-speech narration.
- (Optional) **Gradio / Streamlit** – for building a user interface.

## 🎯 Use Cases

-Quickly get ideas for what to do based on the current weather.
-Get inspired on rainy or sunny days.
-Use as a base for a smart assistant or API integration demo.

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/gonzams8/Planner_App.git
   cd Planner_App
   ```
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Add your API keys to a .env file:
   ```bash
   OPENWEATHER_API_KEY=your_key
   OPENAI_API_KEY=your_key
   ELEVENLABS_API_KEY=your_key
   ```
   
4. Run the app:
   ```bash
   python main.py
   ```
   
## 🖼️ Example
User input: "Santiago, Chile"
Weather: Rainy and 12°C
App response:
"Today is perfect for visiting a local museum, enjoying a hot coffee with a good book, or watching a movie at home. How about a Chilean classic?"
✅ Narrated with human-like voice using ElevenLabs.

## 📁 Project Structure

```bash
📦 voiceweather-planner
├── main.py
├── weather.py
├── planner.py
├── voice.py
├── .env
├── requirements.txt
└── README.md
```

## 🔧 Possible Improvements

- Generate plans based on time of day (morning, afternoon, evening).
- Add multilingual support.
- Build a simple front-end using Gradio or Streamlit.
- Store and display plan history.

## 👤 Author
Gonzalo Mariqueo – [LinkedIn](https://www.linkedin.com/in/gonzalomariqueo/)

**This project is part of my portfolio to demonstrate my skills in API integration, Python automation, and generative AI.**
