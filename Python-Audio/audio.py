from gtts import gTTS
from playsound import playsound  # Ensure playsound==1.2.2 is installed
import os

language = 'en'

while True:
    user_input = input("Enter your words (or type 'exit' to quit): ").strip()
    
    if user_input.lower() in ['exit']:
        print("Exiting...")
        break

    audio = 'speech.mp3'
    sp = gTTS(text=user_input, lang=language, slow=False)
    sp.save(audio)

    playsound(audio)
    print(user_input)

    os.remove(audio)
