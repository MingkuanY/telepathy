raw_input = "testing eleven labs"

#use llama to add spaces



# Import necessary libraries
import requests  # Used for making HTTP requests

# Define constants for the script
CHUNK_SIZE = 1024  # Size of chunks to read/write at a time
XI_API_KEY = "sk_11c8dffc33930f10a61ec0b458405a969cd27c9b8bcc9190"  # Your API key for authentication
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # ID of the voice model to use
TEXT_TO_SPEAK = raw_input  # Text you want to convert to speech
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