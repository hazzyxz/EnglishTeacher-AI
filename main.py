import os
import typer
import speech_recognition as sr
import pyaudio
import pyttsx3
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
app = typer.Typer()
r = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

client = OpenAI(
    api_key=os.environ.get("OPEN_API_KEY")
)

"""Interactive english learning AI"""
typer.echo(
    "\nYour personal AI English teacher is ready, say something! \nSay 'exit' to leave."
)

messages = []

while True:

    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
            text = r.recognize_google(audio)
        
        prompt = text
        messages.append({"role":"user","content":prompt})
        typer.echo(f'\nYou: {prompt}')
    except sr.UnknownValueError:
        r = sr.Recognizer()
        continue
    except sr.RequestError as e:
        continue
    except Exception as e:
        continue


    if prompt == "exit":
        typer.echo("\nTeacher: Goodbye!")
        engine.say("Goodbye!")
        engine.runAndWait()
        break

    response = client.chat.completions.create(
        messages=messages, model="gpt-3.5-turbo"
    )

    ai_reply = response.choices[0].message.content
    typer.echo(f'\nTeacher: {ai_reply}')
    engine.say(ai_reply)
    engine.runAndWait()
    messages.append({"role": "assistant", "content": ai_reply})