import re

def simple_tokens(input_things):
	print type(input_things)
	input_things = [w.replace("I'm", "I am") for w in input_things]

	return input_things