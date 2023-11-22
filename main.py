from tts import text_to_speech, speech_to_text
from messageTrain import *
import sys


def generate_responses():
	reply = get_Message(speech_to_text())
	if reply == "exit":
		print("Program Closed...")
		text_to_speech("Program closed")
		sys.exit(1)
	else:
		text_to_speech(reply)
		generate_responses()


generate_responses()
