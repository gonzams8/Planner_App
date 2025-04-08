from elevenlabs import ElevenLabs
import os
from dotenv import load_dotenv

load_dotenv()

def text_to_speech(plan, output_path='plan.mp3'):
    if not plan:
        print("❌ El texto del plan está vacío. No se generará audio.")
        return None

    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        print("❌ No se encontró la API KEY de ElevenLabs.")
        return None

    client = ElevenLabs(api_key=api_key)

    try:
        # Generador de bytes de audio
        audio_stream = client.text_to_speech.convert(
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            output_format="mp3_44100_128",
            text=plan,
            model_id="eleven_multilingual_v2",
        )

        # Escribir el contenido por partes desde el generador
        with open(output_path, "wb") as f:
            for chunk in audio_stream:
                f.write(chunk)

        print(f"✅ Audio guardado como {output_path}")
        return output_path

    except Exception as e:
        print(f"❌ Error al generar el audio: {e}")
        return None