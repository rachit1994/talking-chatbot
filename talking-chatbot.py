#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
import sys,os
import speech_recognition as sr
import aiml
import pyttsx
import unirest
import json


# obtain audio from the microphone
r = sr.Recognizer()

homedir=os.getcwd();
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
    print("Say something!")
    audio = r.listen(source)
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())

bot = aiml.Kernel();

#bot.learn("wildcard.aiml");

"""list = os.listdir('./aiml-en-us-foundation-alice/');
for item in list:
    bot.learn("aiml-en-us-foundation-alice/" + item);

os.system('cls')

bot.setPredicate("name","alice")
bot.setPredicate("master","rachit")
os.chdir(homedir)
bot.saveBrain("rachit.brn");"""


bot.bootstrap(brainFile = "rachit.brn");

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

text = r.recognize_google(audio);
# These code snippets use an open-source library.
response = unirest.post("https://community-sentiment.p.mashape.com/text/",
  headers={
    "X-Mashape-Key": "6kWx0pf49smshQK5IQRwCyi3Z2S7p1lGNvkjsnvVSC1E4CCCYk",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  },
  params={
    "txt": text
  }
)

os.system('cls')
print (text);
print("response:");
print (response.raw_body);

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`

	print("response",bot.respond(r.recognize_google(audio)));engine.say(bot.respond(r.recognize_google(audio)))
	engine.runAndWait()
except sr.UnknownValueError:
    print("could not understand audio")
except sr.RequestError as e:
    print("Could not request; {0}".format(e))