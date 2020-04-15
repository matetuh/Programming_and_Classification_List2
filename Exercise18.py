import nltk
from nltk.book import *
text = text2
longest = ''
for word in text:
     if len(word) > len(longest):
         longest=word
print(longest)