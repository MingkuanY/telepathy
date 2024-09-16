import requests
from pydub import AudioSegment
from io import BytesIO
import simpleaudio as sa

def authenticate():
    elevenlabs_api_key = "sk_913a0e036c8701dbc7ec3ef355327022e80541b3be01c5bb"
    VOICE_ID = "EXAVITQu4vr4xnSDxMaL"
    
    # Initialize debug and streaming options
    debug = False
    stream = False
    CHUNK_SIZE = 1024

    # Define the Tune API request
    url = "https://proxy.tune.app/chat/completions"
    
  

    # response = requests.post(url, headers=headers, json=data)
    # response = requests.post(url, headers=headers, json=data)
    

    # Convert the summary text to speech using Eleven Labs API
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    headers = {
        "Accept": "application/json",
        "xi-api-key": elevenlabs_api_key
    }
    data = {
        "text": "password authenticated!",
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }
    
    response = requests.post(tts_url, headers=headers, json=data, stream=True)
    
    if response.ok:
        audio_data = response.content
        audio_status = "Audio stream received successfully."
        
        # Convert the audio data (bytes) to a playable audio stream
        audio = AudioSegment.from_file(BytesIO(audio_data), format="mp3")
        
        # Play the audio using simpleaudio
        play_obj = sa.play_buffer(audio.raw_data, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)
        play_obj.wait_done()  # Wait until playback is finished
    else:
        audio_data = None
        audio_status = f"Error in audio generation: {response.text}"
    
    return {
        "audio_status": audio_status
    }