from flask import Flask, request, jsonify, send_file
from apis.tune_weather import generate_audio_and_text
from apis.tune_joke import generate_joke
from apis.capitalOne_show import generate_bank
from apis.tune_news import generate_news
from flask_cors import CORS
import io

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

characters = ""

@app.route('/receive_character', methods=['POST'])
def receive_character():
    global characters
    try:
        data = request.json  # Parse the incoming JSON
        if not data or 'character' not in data:
            return jsonify({"status": "error", "message": "Invalid input"}), 400
        
        character = data["character"]
        characters += character
        return jsonify({"status": "success", "characters": characters}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_characters', methods=['GET'])
def get_characters():
    return jsonify({"characters": characters})

# APIs

@app.route('/w', methods=['POST'])
def w():
    try:
        print("server requested")
        # Call the function to get text and audio
        result = generate_audio_and_text()
        
        # Check if the audio was generated successfully
        if result['audio_data']:
            # Save the audio data to a BytesIO object
            audio_stream = io.BytesIO(result['audio_data'])
            audio_stream.seek(0)  # Ensure the stream is at the beginning

            # Store the audio stream in the Flask app's config for retrieval
            app.config['AUDIO_STREAM'] = audio_stream

            # Return text and the URL to retrieve the audio
            return jsonify({
                'long_text': result['long_text'],
                'summary': result['summary'],
                'audio_url': '/audio'
            }), 200
        else:
            return jsonify({'error': result['audio_status']}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/j', methods=['POST'])
def j():
    print("server requested")
    # Call the function to get text and audio
    result = generate_joke()
    
    # Check if the audio was generated successfully
    if result['audio_data']:
        # Save the audio data to a BytesIO object
        audio_stream = io.BytesIO(result['audio_data'])
        audio_stream.seek(0)  # Ensure the stream is at the beginning

        # Store the audio stream in the Flask app's config for retrieval
        app.config['AUDIO_STREAM'] = audio_stream
    
    print("result: ", result);

    # Return text and the URL to retrieve the audio
    return jsonify({
        'long_text': result['long_text'],
        'summary': result['summary']
    }), 200

@app.route('/s', methods=['POST'])
def s():
    print("server requested")
    # Call the function to get text and audio
    result = generate_bank()
    
    # Check if the audio was generated successfully
    if result['audio_data']:
        # Save the audio data to a BytesIO object
        audio_stream = io.BytesIO(result['audio_data'])
        audio_stream.seek(0)  # Ensure the stream is at the beginning

        # Store the audio stream in the Flask app's config for retrieval
        app.config['AUDIO_STREAM'] = audio_stream
    
    print("result: ", result);

    # Return text and the URL to retrieve the audio
    return jsonify({
        'long_text': result['long_text'],
        'summary': result['summary']
    }), 200

@app.route('/n', methods=['POST'])
def n():
    print("server requested")
    # Call the function to get text and audio
    result = generate_news()
    
    # Check if the audio was generated successfully
    if result['audio_data']:
        # Save the audio data to a BytesIO object
        audio_stream = io.BytesIO(result['audio_data'])
        audio_stream.seek(0)  # Ensure the stream is at the beginning

        # Store the audio stream in the Flask app's config for retrieval
        app.config['AUDIO_STREAM'] = audio_stream
    
    print("result: ", result);

    # Return text and the URL to retrieve the audio
    return jsonify({
        'long_text': result['long_text'],
        'summary': result['summary']
    }), 200

app.run(port=4000)