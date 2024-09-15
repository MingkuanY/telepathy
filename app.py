from flask import Flask, request, jsonify, send_file
from apis.tune_weather import generate_audio_and_text
from flask_cors import CORS
import subprocess
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
        # Call the function to get text and audio
        result = generate_audio_and_text()
        
        # Check if the audio was generated successfully
        if result['audio_data']:
            # Save the audio data to a BytesIO object
            audio_stream = io.BytesIO(result['audio_data'])
            audio_stream.seek(0)  # Ensure the stream is at the beginning

            # Return text and audio file path
            return jsonify({
                'long_text': result['long_text'],
                'summary': result['summary'],
                'audio_url': '/audio'
            }), 200

        else:
            return jsonify({'error': result['audio_status']}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/audio')
def audio():
    # Retrieve the audio stream from the app configuration
    audio_stream = app.config.get('AUDIO_STREAM')
    if audio_stream:
        audio_stream.seek(0)
        return send_file(audio_stream, mimetype='audio/mpeg', as_attachment=True, attachment_filename='output.mp3')
    else:
        return jsonify({'error': 'No audio available'}), 404

if __name__ == '__main__':
    app.run(port=4000)
