import nltk
from nltk.book import *
import string

# clearing unwanted signs
sign = str.maketrans('','','--')
text2 = [x.translate(sign) for x in text2]

text = ""
for x in text2:
    if x in string.punctuation or x == "s":
        text = text + x
    else:
        text = text + " " + x

#tokenizing sentences
text3 = nltk.sent_tokenize(text)
#the max lenght of sentence
length_text3 = lambda text3: len(nltk.word_tokenize(text3))

#choosing the sentnce of max length
max_lengt_text = max(text3, key=length_text3)

#printing longest text
print(max_lengt_text)