# Audio to Text Transcription App

A Flask-based web application that converts audio files to text using OpenAI's Whisper API. This application provides a simple interface for users to upload MP3 files and receive accurate text transcriptions.

## Features

- Upload MP3 audio files (up to 16MB)
- Transcribe audio to text using OpenAI's Whisper API
- Simple and intuitive web interface
- Secure file handling with temporary storage
- Error handling and logging

## Prerequisites

- Python 3.11 or higher
- OpenAI API key
- pipenv (for dependency management)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd audio-to-text
```

2. Install dependencies using pipenv:
```bash
pipenv install
```

3. Create a `.env` file in the root directory and add your configuration:
```
OPENAI_API_KEY=your_openai_api_key_here
SESSION_SECRET=your_session_secret_here
```

## Usage

1. Activate the virtual environment:
```bash
pipenv shell
```

2. Run the application:
```bash
python main.py
```

3. Open your web browser and navigate to `http://localhost:5000`

4. Upload an MP3 file and wait for the transcription

## API Endpoints

- `GET /`: Renders the main application page
- `POST /upload`: Accepts MP3 file uploads and returns transcribed text
  - Request: multipart/form-data with 'audio' field
  - Response: JSON containing transcribed text or error message

## Technical Details

- Built with Flask web framework
- Uses OpenAI's Whisper API for accurate audio transcription
- Implements secure file handling with `werkzeug`
- Includes logging for debugging and monitoring
- Environment variables managed with python-dotenv

## File Structure

```
audio-to-text/
├── app.py           # Main application file
├── utils.py         # Utility functions
├── static/          # Static assets
├── templates/       # HTML templates
├── Pipfile         # Dependencies
├── Pipfile.lock    # Locked dependencies
└── .env            # Environment variables (not tracked in git)
```

## Security Features

- Secure filename handling
- Temporary file storage with automatic cleanup
- File size limitations (16MB max)
- File type restrictions (MP3 only)
- Environment variable based configuration

## Error Handling

The application includes comprehensive error handling for:
- Missing files
- Invalid file types
- File size exceeded
- API transcription failures
- Server errors

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License
