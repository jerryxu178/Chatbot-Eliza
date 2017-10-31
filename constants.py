
"""
patterns_list contains the patterns that the chatbot needs for pattern matching.

patterns_list is implemented as a list of tuples, where the first element of 
each tuple is a pattern that may match the user's statement and the second
element is a list of responses that the chatbot may choose from.
"""

patterns_list = [
	(r'i need (.*)', 
	["Why do you need {}?", 
	"Would it really help you to get {}?",
	"Are you sure you need {}?"]),

	(r'why don\'?t you ([^\?]*)\??',
		["Do you really think I don't {}?",
		"Perhaps eventually I will {}.",
		"Do you really want me to {}?"]),

	(r'why can\'?t i ([^\?]*)\??',
		["Do you think you should be able to {}?",
		"If you could {}, what would you do?",
		"I don't know... why can't you {}?",
		"Have you really tried?"
		]),

	(r'i can\'?t (.*)',
		["How do you know you can't {}?",
		"Perhaps you could {} if you tried.",
		"What would it take for you to {}?"
		]),

	(r'i am (.*)',
		["Did you come to me because you are {}?",
		"How long have you been {}?",
		"How do you feel about being {}?"]),

	(r'i\'?m (.*)',
		["How does being {} make you feel?",
		"Do you enjoy being {}?",
		"Why do you tell me you're {}?",
		"Why do you think you're {}?"]),

	(r'are you ([^\?]*)\??',
		["Why does it matter whether I am {}?",
		"Would you prefer it if I were not {}?",
		"Perhaps you believe I am {}.",
		"I may be {} -- what do you think?"]),

	(r'what (.*)',
		["Why do you ask?",
		"How would an answer to that help you?",
		"What do you think?"]),

	(r'how (.*)',
		["How do you suppose?",
		"Perhaps you can answer your own question.",
		"What is it you're really asking?"]),

	(r'Because (.*)',
		["Is that the real reason?",
		"What other reasons come to mind?",
		"Does that reason apply to anything else?",
		"If {}, what else must be true?"]),

	(r'(.*) sorry (.*)',
		["There are many times when no apology is needed.",
		"What feelings do you have when you apologize?"]),

	(r'hello(.*)',
		["Hello... I'm glad you could drop by today.",
		"Hi there... how are you today?",
 		"Hello, how are you feeling today?"]),

	(r'i think (.*)',
		["Do you doubt {}?",
		"Do you really think so?",
		"But you're not sure {}?"]),

	(r'(.*) friend (.*)',
		["Tell me more about your friends.",
		"When you think of a friend, what comes to mind?",
		"Why don't you tell me about a childhood friend?"]),

	(r'yes',
		["You seem quite sure.",
		"OK, but can you elaborate a bit?"]),
 
	(r'(.*) computer(.*)',
		["Are you really talking about me?",
		"Does it seem strange to talk to a computer?",
		"How do computers make you feel?",
		"Do you feel threatened by computers?"]),

	(r'is it (.*)',
		["Do you think it is {}?",
		"Perhaps it's {} -- what do you think?",
		"If it were {}, what would you do?",
		"It could well be that {}."]),

	(r'it is (.*)',
		["You seem very certain.",
		"If I told you that it probably isn't {}, what would you feel?"]),

	(r'can you ([^\?]*)\??',
		["What makes you think I can't {}?",
		"If I could {}, then what?",
		"Why do you ask if I can {}?"]),

	(r'can i ([^\?]*)\??',
		["Perhaps you don't want to {}.",
		"Do you want to be able to {}?",
		"If you could {}, would you?"]),

	(r'you are (.*)',
		["Why do you think I am {}?",
		"Does it please you to think that I'm {}?",
		"Perhaps you would like me to be {}.",
		"Perhaps you're really talking about yourself?"]),

	(r'you\'?re (.*)',
		["Why do you say I am {}?",
		"Why do you think I am {}?",
		"Are we talking about you, or me?"]),

	(r'i don\'?t (.*)',
		["Don't you really {}?",
		"Why don't you {}?",
		"Do you want to {}?"]),

	(r'i feel (.*)',
		["Good, tell me more about these feelings.",
		"Do you often feel {}?",
		"When do you usually feel {}?",
		"When you feel {}, what do you do?"]),

	(r'i have (.*)',
		["Why do you tell me that you've {}?",
		"Have you really {}?",
		"Now that you have {}, what will you do next?"]),

	(r'i would (.*)',
		["Could you explain why you would {}?",
		"Why would you {}?",
		"Who else knows that you would {}?"]),

	(r'is there (.*)',
		["Do you think there is {}?",
		"It's likely that there is {}.",
		"Would you like there to be {}?"]),

	(r'you (.*)',
		["We should be discussing you, not me.",
		"Why do you say that about me?",
		"Why do you care whether I {}?"]),

	(r'why (.*)',
		["Why don't you tell me the reason why {}?",
		"Why do you think {}?"]),

	(r'i want (.*)',
		["What would it mean to you if you got {}?",
		"Why do you want {}?",
		"What would you do if you got {}?",
		"If you got {}, then what would you do?"]),

	(r'(.*) mother(.*)',
		["Tell me more about your mother.",
		"What was your relationship with your mother like?",
		"How do you feel about your mother?",
		"How does this relate to your feelings today?",
		"Good family relations are important."]),

	(r'(.*) father(.*)',
		["Tell me more about your father.",
		"How did your father make you feel?",
		"How do you feel about your father?",
		"Does your relationship with your father relate to your feelings today?",
		"Do you have trouble showing affection with your family?"]),

	(r'(.*) child(.*)',
		["Did you have close friends as a child?",
		"What is your favorite childhood memory?",
		"Do you remember any dreams or nightmares from childhood?",
		"Did the other children sometimes tease you?",
		"How do you think your childhood experiences relate to your feelings today?"]),

	(r'(.*)\?',
		["Why do you ask that?",
		"Please consider whether you can answer your own question.",
		"Perhaps the answer lies within yourself?",
		"Why don't you tell me?"]),

	(r'quit',
		["Thank you for talking with me.",
		"Good-bye.",
		"Thank you, that will be $150.  Have a good day!"]),

	(r'foo',
		["foo to you too!"]),

	(r'(.*)',
		["Please tell me more.",
		"Let's change focus a bit... Tell me about your family.",
		"Can you elaborate on that?",
		"Why do you say that {}?",
		"I see.",
		"Very interesting.",
		"{}.",
		"I see.  And what does that tell you?",
		"How does that make you feel?",
		"How do you feel when you say that?"])
]


"""
reflections_dict is a dictionary that the chatbot uses to convert words so that
statements that are echoed back to the user make sense.

Example: 
Suppose the user input is "the wallet is mine". The chatbot will use
reflections_dict to convert "mine"->"yours" in order to generate the response
"Is the wallet really yours?"

"""

reflections_dict = {
	"i": "you",
	"i'd": "you would",
	"i've": "you have",
	"i'll": "you will",
	"you": "me", 
	"you've": "I have",
	"you'll": "I will",
	"you'd": "I would",
	"your": "my",
	"yours": "mine",
	"me": "you",
	"my": "your",
	"mine": "yours", 
	"am": "are",
	"are": "am",
	"was": "were",
	"were": "was" 
}

