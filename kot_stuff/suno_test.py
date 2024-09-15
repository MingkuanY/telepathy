import requests

# API endpoint and headers
url = 'https://studio-api.suno.ai/api/external/generate/'

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'affiliate-id': 'undefined',
    'authorization': 'Bearer A9CaGEYEOqFkKLf6CnCwGmuZuBj6f96C',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://suno.com/',
    'referer': 'https://suno.com/',
}

# Data payload (song topic and tags)
payload = {
    "topic": "A song about traveling on Christmas",
    "tags": "pop"
}

# Send POST request
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    result = response.json()
    print("Response:", result)
    
    # # Print relevant fields directly
    # print(f"Song ID: {result.get('id', 'N/A')}")
    # print(f"  Title: {result.get('title', 'N/A')}")
    # print(f"  Lyric: {result.get('metadata', {}).get('prompt', 'N/A')}")
    # print(f"  Audio URL: {result.get('audio_url', 'N/A')}")
    # print(f"  Video URL: {result.get('video_url', 'N/A')}")
    # print(f"  Created At: {result.get('created_at', 'N/A')}")
    # print(f"  Model Name: {result.get('metadata', {}).get('type', 'N/A')}")
    # print(f"  Status: {result.get('status', 'N/A')}")
    # print(f"  GPT Prompt: {result.get('metadata', {}).get('gpt_description_prompt', 'N/A')}")
        
    # If audio_url exists, download the audio
    if result.get('audio_url'):
        audio_url = result['audio_url']
        print("Downloading audio from:", audio_url)
        audio_response = requests.get(audio_url)
        audio_filename = f"song_{result['id']}.mp3"
        with open(audio_filename, 'wb') as audio_file:
            audio_file.write(audio_response.content)
        print(f"Audio file saved as {audio_filename}")
    else:
        print("no audio url :( \n\n")
else:
    print(f"Error: {response.status_code}, {response.text}")
