import json
import requests
from pydub import AudioSegment
from io import BytesIO
import simpleaudio as sa

def generate_bank():
    # Hardcoded values
    card_id = "66e601b79683f20dd5189be3" #this is Alex's credit card
    url = f"http://api.nessieisreal.com/accounts/{card_id}/deposits?key=2bc034cd8680c577516f30dfe52a67ff"

    response = requests.get(url, headers={'Accept': 'application/json'})

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response and print it
        transactions = response.json()
        print(json.dumps(transactions, indent=4))
        context = transactions
    else:
        context = "Failed to fetch transactions"


    user_prompt = f"Using the given context, tell me about my deposits: {context}. IGNORE the transaction STATUS. SHOULD BE LESS THAN 2 SENTENCES"
    
    tune_api_key = "sk-tune-3AlBdVNL1WlF9KJyd7Ms5asst5S75L0WqLv"
    elevenlabs_api_key = "sk_edd71416ad1a81f444fb057e235b62f3a61dbec817e4089e"
    VOICE_ID = "EXAVITQu4vr4xnSDxMaL"
    
    # Initialize debug and streaming options
    debug = False
    stream = False
    CHUNK_SIZE = 1024

    # Define the Tune API request
    url = "https://proxy.tune.app/chat/completions"
    headers = {
        "Authorization": tune_api_key,
        "Content-Type": "application/json",
    }
    
    # Send user prompt to Tune API
    data = {
        "temperature": 0.8,
        "messages": [
            {
                "role": "user",
                "content": user_prompt
            },
        ],
        "model": "kaushikaakash04/tune-blob",
        "stream": stream,
        "frequency_penalty": 0,
        "max_tokens": 100
    }

    response = requests.post(url, headers=headers, json=data)
    
    if stream:
        output = ''
        for line in response.iter_lines():
            if line:
                l = line[6:]
                if l != b'[DONE]':
                    output += json.loads(l)['choices'][0]['message']['content']
    else:
        full_json_output = response.json()
        output = full_json_output['choices'][0]['message']['content']
        print("\n\nMIDDLE PART:")
        print(output)

    
   
    response = requests.post(url, headers=headers, json=data) #TODO idk what this is
    
    
    # Convert the summary text to speech using Eleven Labs API
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    headers = {
        "Accept": "application/json",
        "xi-api-key": elevenlabs_api_key
    }
    data = {
        "text": output,
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
        "summary": output,
        "audio_status": audio_status
    }