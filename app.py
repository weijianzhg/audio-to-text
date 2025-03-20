import os
import logging
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import tempfile
from utils import is_allowed_file, transcribe_audio_file
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

# Configure upload settings
ALLOWED_EXTENSIONS = {'mp3'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audio' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['audio']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not is_allowed_file(file.filename, ALLOWED_EXTENSIONS):
        return jsonify({'error': 'Invalid file type. Only MP3 files are allowed'}), 400

    try:
        # Create temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
            file.save(temp_file.name)

            # Process the audio file
            transcribed_text = transcribe_audio_file(temp_file.name)

            # Clean up the temporary file
            os.unlink(temp_file.name)

            return jsonify({
                'success': True,
                'text': transcribed_text
            })

    except Exception as e:
        logger.error(f"Error processing audio file: {str(e)}")
        return jsonify({
            'error': 'Failed to process audio file. Please try again.'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
