import re
import random
from constants import reflections_dict, patterns_list


def reflect(fragment):
	"""
	documentation here
	"""
	return fragment

def generate_response(statement):
	"""
	documentation here
	"""
	for pattern, responses in patterns_list:
		match = re.match(pattern, statement.rstrip(".!?")) # match is None or a Match object
		if match:
			response = random.choice(responses) # response with {} as placeholder for user text
			fragment = reflect(match.group(1)) # piece of user text to be echoed back in response
			# convert "I" to "you", and other similar changes
			return response.format(fragment)

def main():
	print "Hello. How are you feeling today?"
	while True:
		statement = raw_input(">")
		print generate_response(statement.lower())

if __name__ == "__main__":
	main()