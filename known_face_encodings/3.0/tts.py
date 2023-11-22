# import python text to speech
import pyttsx3
import speech_recognition as sr

# Initialize pyttsx3 and recognizer classes (for recognizing the speech)

r = sr.Recognizer()
tts_engine = pyttsx3.init()

def tts_init(num):
	try:
		tts_engine.say(num)
	except:
		print("TTS Engine is down..!!!")
	tts_engine.runAndWait()

def stt_init():
	with sr.Microphone() as source:
		print("Listening...")
		audio_text = r.listen(source)
		print("Processing...")
		# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
		try:
			# using google speech recognition
			reply = r.recognize_google(audio_text)
			if reply.find("exit") != -1 and len(reply) <= 6:
				return "0X26h45"
			else:
				return reply
		except sr.UnknownValueError:
			return "Could not understand audio"
		except sr.RequestError as e:
			return "Request failed, Check your internet connection"
