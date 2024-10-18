import pprint
from collections import defaultdict
import string
import sys

SENTENCE = input("Enter the text you would like to analyze: ").lower()
'''TRANSLATOR1 = str.maketrans('', '', string.punctuation)
print("TRANSLATOR1=", TRANSLATOR1)
TRANSLATOR2 = str.maketrans('', '', string.whitespace)
print("TRANSLATOR2=", TRANSLATOR2)
WITHOUT_PUNCT = SENTENCE.translate(TRANSLATOR1)
print("WITHOUT_PUNCT=", WITHOUT_PUNCT)
WITHOUT_WHITESPACE = WITHOUT_PUNCT.translate(TRANSLATOR2)
print("WITHOUT_WHITESPACE=", WITHOUT_WHITESPACE)
s = list(WITHOUT_WHITESPACE)
d = defaultdict(list)
'''
#pp = pprint.PrettyPrinter()

m = defaultdict(list)
for k in SENTENCE:
    k=k.lower()
    m[k].append(k)
    
print("\nYou may need to stretch console window if text wrapping occurs.\n")
print("text = ", end='')
print("{}\n".format(SENTENCE), file=sys.stderr)
pprint.pprint(m, width=110)
