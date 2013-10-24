import sys
import nltk.data
from nltk.tokenize import whitespace_tokenize
import simple_tokens

input_file = open(sys.argv[1]).read()
input_file = simple_tokens.simple_tokens(input_file)
input_file = whitespace_tokenize(input_file)
input_file = [w.lower() for w in input_file if w.isalpha()]
basic_english = nltk.corpus.words.words('en-basic')

nonsimple_words = tuple(set(input_file) - set(basic_english))
print("Total number of words: ")
print(len(input_file))
print("Nonsimple words: ")
print(nonsimple_words)

percent = 100 - (float(len(nonsimple_words)) / float(len(input_file))) * 100
print("Percentage simple english: (v0.1)")
print(percent)

