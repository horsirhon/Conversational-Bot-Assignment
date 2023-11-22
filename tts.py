# import python text to speech
import pyttsx3
import speech_recognition as sr

# Initialize pyttsx3 and recognizer classes (for recognizing the speech)


tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 180)
r = sr.Recognizer()
r.pause_threshold = 2


def text_to_speech(words):
	try:
		tts_engine.say(words)
	except:
		print("TTS Engine is down..!!!")
	tts_engine.runAndWait()


def speech_to_text():
	with sr.Microphone() as source:
		print("Listening")
		try:
			audio = r.listen(source)
			reply = list(r.recognize_google(audio, with_confidence=True))[0]
			if reply.find("exit") != -1:
				return "exit"
			return reply
		except sr.UnknownValueError:
			return "Could not understand audio"
		except sr.RequestError as e:
			return "Could not request results from Google Speech Recognition service; {0}".format(e)

