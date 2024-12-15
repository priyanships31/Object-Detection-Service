from flask import Flask, request, jsonify, render_template, send_file
import requests
import logging
import os

# Initialize Flask app
app = Flask(__name__, static_folder='.')

# AI backend URL (ensure this matches your setup)
AI_BACKEND_URL = 'http://ai_backend:5001/detect'

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Ensure output directory exists
os.makedirs('output', exist_ok=True)

@app.route('/')
def home():
    logger.info("Rendering home page (index.html)")
    return render_template('index.html')

@app.route('/output/<filename>')
def serve_output_image(filename):
    try:
        return send_file(os.path.join('output', filename))
    except FileNotFoundError:
        logger.error(f"Image not found: {filename}")
        return jsonify({'error': 'Image not found'}), 404

@app.route('/upload', methods=['POST'])
def upload_image():
    logger.info("Received POST request to /upload endpoint")
    file = request.files.get('image')
    if not file:
        logger.error("No image uploaded in the request")
        return jsonify({'error': 'No image uploaded'}), 400

    logger.debug(f"Uploaded file: {file.filename}, Content-Type: {file.content_type}")

    try:
        logger.info(f"Forwarding image to AI backend at {AI_BACKEND_URL}")
        response = requests.post(AI_BACKEND_URL, files={'image': (file.filename, file.stream, file.content_type)})

        logger.debug(f"Response received from AI backend: Status Code {response.status_code}")
        if response.status_code == 200:
            logger.info("Successfully processed the image via AI backend")
            result = response.json()
            
            # Ensure we're using just the filename
            output_image = os.path.basename(result.get('output_image', 'default_image.jpg'))
            result['output_image'] = f"output/{output_image}"

            return jsonify(result)
        else:
            logger.error(f"AI backend returned an error: {response.text}")
            return jsonify({'error': 'AI backend processing failed'}), response.status_code
    except requests.exceptions.RequestException as e:
        logger.exception(f"Failed to communicate with AI backend: {e}")
        return jsonify({'error': 'Failed to communicate with AI backend'}), 500
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    logger.info("Starting UI backend service on http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)


