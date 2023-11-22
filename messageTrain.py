from openaiget import openaiAPIget


message_train = [
	{
		"role": "user",
		"content": "My name is Osahon. Your name is Botbot. make your replies short and conversational"
	}
]


def get_Message(text, mode=True):
	if text == "exit":
		return text
	print("Osahon: " + text + "\n")
	if mode:
		message_train.append({
			"role": "user",
			"content": text
		})
		message_train.append({
			"role": "user",
			"content": text
		})
	reply = openaiAPIget(message_train)
	print("Botbot: " + reply)

	return reply

