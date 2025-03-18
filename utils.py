import os
from openai import OpenAI
import logging

logger = logging.getLogger(__name__)

def is_allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

def transcribe_audio_file(file_path):
    """
    Transcribe audio file using OpenAI Whisper API
    """
    try:
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        
        with open(file_path, "rb") as audio_file:
            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return response.text
    except Exception as e:
        logger.error(f"Transcription error: {str(e)}")
        raise Exception("Failed to transcribe audio file")
