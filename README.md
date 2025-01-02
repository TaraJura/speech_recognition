# Speech Recognition Project

Simple speech recognition application that listens to Czech speech input and converts it to text using Google's Speech Recognition API.

## Prerequisites

- Ubuntu/Debian-based system
- Python 3.x
- Git

## Installation

1. Clone the repository:
```bash
git clone git@github.com:TaraJura/speech_recognition.git
cd speech_recognition
```

2. Install system dependencies:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv portaudio19-dev python3-pyaudio
```

3. Create and activate virtual environment:
```bash
python3 -m venv myenv
source myenv/bin/activate
```

4. Install Python dependencies:
```bash
pip install SpeechRecognition pyaudio
```

## Usage

1. Make sure your virtual environment is activated:
```bash
source myenv/bin/activate
```

2. Run the script:
```bash
python3 speech.py
```

3. Start speaking in Czech when you see "Čekám na tvůj hlas..." (Waiting for your voice...)

4. The application will:
   - Listen for your speech input
   - Convert it to text using Google's Speech Recognition
   - Display the recognized text
   - Continue listening until interrupted

5. To stop the application, press `Ctrl+C`

## Development

To save your project dependencies:
```bash
pip freeze > requirements.txt
```

## Troubleshooting

If you encounter issues with PyAudio installation:
1. Ensure you have installed `portaudio19-dev`
2. Try reinstalling PyAudio:
```bash
pip uninstall pyaudio
pip install pyaudio
```

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]