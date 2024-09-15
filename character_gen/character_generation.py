import random
import string
import time
from convex import ConvexClient

# Initialize the Convex client with your Convex deployment URL
client = ConvexClient("https://uncommon-heron-546.convex.cloud")

# Function to generate a random character (a-z, 0-9)
def generate_character():
    characters = string.ascii_lowercase + string.digits
    return random.choice(characters)

# Main loop to generate a character every 2 seconds and save it to Convex DB
def generate_and_save_character():
    while True:
        # Generate a random character
        character = generate_character()
        
        # Get the current timestamp in milliseconds
        timestamp = int(time.time() * 1000)
        
        # Save the character and timestamp to the Convex database
        client.mutation('saveCharacter', {"character": character, "timestamp": timestamp})
        
        print(f"Generated and saved to Convex: {{'character': '{character}', 'timestamp': {timestamp}}}")
        
        # Wait for 2 seconds before generating the next character
        time.sleep(2)

# Run the character generation loop
if __name__ == '__main__':
    generate_and_save_character()
