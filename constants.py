
"""
patterns_list contains the patterns that the chatbot needs for pattern matching.

patterns_list is implemented as a list of lists, where each element contains a 
pattern that may match the user's statement and also a list of responses that
the chatbot choose from to echo back the user's original statement.
"""
patterns_list = [
	(r'i need (.*)', # NOTE: switch to tuple here? need to update documentation
	["Why do you need {}?", # NOTE: changed {0} -> {}
	"Would it really help you to get {}?",
	"Are you sure you need {}?"]),

	(r'why don\'?t you ([^\?]*)\??',
		["Do you really think I don't {}?",
		"Perhaps eventually I will {}.",
		"Do you really want me to {}?"])



	
]


"""
reflections_dict is a dictionary that the chatbot uses to convert words so that
statements that are echoed back to the user make sense.

MORE EXPLANATION HERE. MAYBE AN EXAMPLE
"""
reflections_dict = {
	"i": "you",
	"i'd": "you would",
	"i've": "you have",
	"i'll": "you will",
	"you": "me", # check this... me or I
	"you've": "I have",
	"you'll": "I will",
	"you'd": "I would",
	"your": "my",
	"yours": "mine",
	"me": "you",
	"my": "your",
	"mine": "yours", # check this 
	"am": "are",
	"are": "am",
	"was": "were",
	"were": "was" # check this
}






