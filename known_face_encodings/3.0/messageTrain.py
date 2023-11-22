from openaiget import openaiAPIget


message_train = [
	{
		"role": "user",
		"content": "My name is Osahon. make your replies as short as possible."
	}
]


def do_this(text, mode=True):
	if text == "0X26h45":
		return text
	print("User: " + text + "\n" )
	reply = openaiAPIget(message_train)
	if mode:
		message_train.append({
			"role": "user",
			"content": text
		})
		message_train.append({
			"role": "assistant",
			"content": reply
		})
	print("Assistant: " + reply)
	return reply

