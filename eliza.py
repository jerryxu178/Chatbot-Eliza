import re
import random
from constants import reflections_dict, patterns_list


def reflect(fragment):
	"""
	reflect takes a string and replaces any words that have a corresponding
	reflection. For example, "my house" is returned as "your house". 

	reflect() looks up reflections in reflections_dict, and is used in 
	generate_response()
	"""
	word_list = fragment.split(" ")
	for index in range(len(word_list)):
		word = word_list[index]
		if word in reflections_dict:
			word_list[index] = reflections_dict[word]
	return " ".join(word_list)

def generate_response(statement):
	"""
	generate_response takes the input string and returns a response, based on
	the patterns that the input matches. The returned response takes the form
	of a string.
	"""
	for pattern, responses in patterns_list:
		match = re.match(pattern, statement.rstrip(".!?")) 
		if match:
			# response is the bot's reply, with {} as placeholder for user text
			response = random.choice(responses) 
			try:
				# fragment contains the piece of user text to be echoed back
				fragment = reflect(match.group(1)) 
			except IndexError:
				fragment = ""
			# convert "I" to "you", and other similar changes
			return response.format(fragment)

def main():
	print "Hello. How are you feeling today?"
	while True:
		statement = raw_input(">")
		print generate_response(statement.lower())
		if statement.lower() == "quit":
			break

if __name__ == "__main__":
	main()