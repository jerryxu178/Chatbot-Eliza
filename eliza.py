import re
import random
from constants import reflections_dict, patterns_list

def generate_response(statement):
	for pattern, responses in patterns_list:
		re.match(pattern, statement.rstrip(".!?"))

def main():
	print "Hello. How are you feeling today?"
	while True:
		statement = raw_input(">")
		print generate_response(statement.lower())

if __name__ == "__main__":
	main()