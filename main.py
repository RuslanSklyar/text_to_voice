import pyttsx3
from gtts import gTTS
from tqdm import tqdm
from time import sleep

engine = pyttsx3.init()

file_path = "text.txt"
file = open(file_path, "r")

the_text = file.read()

engine.say(the_text)
engine.runAndWait()
file.close()

for i in tqdm(range(100)):
    sleep(0.01)

tts = gTTS(text=the_text, lang="ru")
tts.save("file.wav")
