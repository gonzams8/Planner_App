def text_to_speech(plan, output_path='plan.mp3'):

    from elevenlabs import ElevenLabs
    import os

    if not plan or not plan.strip():
        print("❌ El plan está vacío. No se generará audio.")
        return None

    client = ElevenLabs(
        api_key="ELEVENLABS_API_KEY",
    )

    try:
        audio = client.text_to_speech.convert(
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            output_format="mp3_44100_128",
            text=plan,
            model_id="eleven_multilingual_v2",
        )

        #guardar el audio en archivo
        with open(output_path, "wb") as f:
            f.write(audio)

        print(f"✅ Audio guardado como {output_path}")
        return output_path
    
    except Exception as e:
        print(f"❌ Error al generar el audio: {e}")
        return None