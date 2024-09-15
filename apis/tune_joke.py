import json
import requests

tune_api_key = "sk-tune-3AlBdVNL1WlF9KJyd7Ms5asst5S75L0WqLv"
elevenlabs_api_key = "sk_edd71416ad1a81f444fb057e235b62f3a61dbec817e4089e"


debug = False

if debug:
    user_prompt = "test"
else:
    user_prompt = "Tell me a joke!"

stream = False #Can toggle true or false here
url = "https://proxy.tune.app/chat/completions"
headers = {
    "Authorization": tune_api_key, #tune API key
    "Content-Type": "application/json",
}
data = {
  "temperature": 0.8,
    "messages":  [
        {
            "role": "user",
            "content": user_prompt
        },
    ],
    "model": "kaushikaakash04/tune-blob",
    "stream": stream,
    "frequency_penalty":  0,
    "max_tokens": 100
}

response = requests.post(url, headers=headers, json=data)
if stream:
    for line in response.iter_lines():
        if line:
            l = line[6:]
            if l != b'[DONE]':
              print(json.loads(l))
else:
    full_json_output = response.json()
    full_output = full_json_output['choices'][0]['message']['content']
    print(full_output)
    
    

# ELEVEN LABS
# Import necessary libraries
import requests  # Used for making HTTP requests

# Define constants for the script
CHUNK_SIZE = 1024  # Size of chunks to read/write at a time
XI_API_KEY = elevenlabs_api_key  # Your API key for authentication
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # ID of the voice model to use
TEXT_TO_SPEAK = full_output  # Text you want to convert to speech
OUTPUT_PATH = "output.mp3"  # Path to save the output audio file

#VOICE IDs
# Antoni: ErXwobaYiN019PkySvjV
# Arnold: VR6AewLTigWG4xSOukaG
# Bella: EXAVITQu4vr4xnSDxMaL
# Charlotte: XB0fDUnXU5powFXDhCwa
# Clyde: 2EiwWnXFnvU5JabPnv8n
# Daniel: onwK4e9ZLuTAKqWW03F9
# James: ZQe5CZNOzWyzPSCn5a3c
# Mimi: zrHiDhphv9ZnVXBqCLjz

# Construct the URL for the Text-to-Speech API request
tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

# Set up headers for the API request, including the API key for authentication
headers = {
    "Accept": "application/json",
    "xi-api-key": XI_API_KEY
}

# Set up the data payload for the API request, including the text and voice settings
data = {
    "text": TEXT_TO_SPEAK,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.8,
        "style": 0.0,
        "use_speaker_boost": True
    }
}

# Make the POST request to the TTS API with headers and data, enabling streaming response
response = requests.post(tts_url, headers=headers, json=data, stream=True)

# Check if the request was successful
if response.ok:
    # Open the output file in write-binary mode
    with open(OUTPUT_PATH, "wb") as f:
        # Read the response in chunks and write to the file
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            f.write(chunk)
    # Inform the user of success
    print("Audio stream saved successfully.")
else:
    # Print the error message if the request was not successful
    print(response.text)