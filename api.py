from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import main
import os

app = Flask(__name__, static_folder='Sticker_Generator/data')
CORS(app)

@app.route('/generate-sticker', methods=['POST'])
def generate_sticker_endpoint():
    data = request.get_json()
    sticker_url = main.generate_sticker(data)
    # background_removal_type = 'AI' if data.get("background_removal_method", "AI") == "AI" else 'Standard'
    return jsonify({'sticker_url': f'{sticker_url}'})

@app.route('/Sticker_Generator/data/<path:path>')
def serve_static(path):
    return send_from_directory(os.path.join(app.static_folder), path)

if __name__ == '__main__':
    app.run(debug=True)
