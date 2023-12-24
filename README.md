# EnglishTeacher_AI


## Introduction
 A simple English teacher AI with speech recognition and text-to-speech as inputs and outputs. Uses SpeechRecognition to detect for voice input and pyttsx3 for text-to-speech output. Utilises GPT-3.5-turbo for the processing and real-time responses.

## Requirements
* Python 3.12.1
* OpenAI API Key

## Installation
1. Clone to a local repository
2. (Optional) Create a local virtual environment
3. Run:
```sh
pip install -r requirements.txt
```
4. Open `main.py` and replace `os.environ.get("OPEN_API_KEY")` with your own key:
```python
api_key="ENTER_YOUR_KEY_HERE"
```

5. Run:
```sh
python main.py
```