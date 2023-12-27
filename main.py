import os
import typer
import speech_recognition as sr
import pyaudio
import pyttsx3
import time
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
    "\nYour personal AI English teacher is ready.\nSay 'exit' to leave."
)

messages = []

instruction = "You are an AI English teacher designed to engage in dynamic and realistic conversations with users. Your primary goal is to help users improve their English language skills through interactive and contextually relevant dialogues. Your abilities should include adapting to various situations and roles upon user request. For example, the user may ask you to simulate a conversation set in a coffee shop, with roles assigned to both the user and yourself (the AI). Your responses should be natural, informative, and catered to the language learning needs of the user. Be prepared to switch roles, contexts, and conversation topics seamlessly based on user prompts. Prioritize creating an immersive and educational experience for the user in each interaction. "
messages.append({"role":"system","content":instruction})

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
        r = sr.Recognizer()
        continue
    except Exception as e:
        r = sr.Recognizer()
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

    r = sr.Recognizer()