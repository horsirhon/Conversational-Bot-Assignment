from tts import tts_init, stt_init
from messageTrain import *


def run_till():
	reply = do_this(stt_init())
	if reply == "0X26h45":
		print("Program Closed...")
		tts_init("Program closed")
	else:
		tts_init(reply)
		run_till()


run_till()
