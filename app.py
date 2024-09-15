from flask import Flask, request, jsonify
from flask_cors import CORS

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

if __name__ == '__main__':
    app.run(port=4000)
