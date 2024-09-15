import random
import string
import time
import requests
import json

# Function to generate a random character (a-z, 0-9)
def generate_character():
    characters = string.ascii_lowercase + string.digits
    return random.choice(characters)

# Function to send the character to the Flask server
def send_character_to_flask(character):
    url = "http://localhost:4000/receive_character"
    payload = json.dumps({"character": character})
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()  # Raise exception if the request failed
        success = "Successfully sent character to Flask"
    except requests.exceptions.RequestException as e:
        error = "Error sending character to Flask: {e}"

# Main loop to generate a character every 2 seconds and send it to Flask
def generate_and_send_character():
    while True:
        # Generate a random character
        character = generate_character()
        
        # Send the character to Flask
        send_character_to_flask(character)
        
        # Wait for 2 seconds before generating the next character
        time.sleep(2)

# Run the character generation loop
if __name__ == "__main__":
    generate_and_send_character()
