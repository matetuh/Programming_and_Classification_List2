#importing libraries
import nltk
from nltk.corpus import stopwords 
import pandas as pd
from tika import parser
from nltk.stem import PorterStemmer 

text = parser.from_file('D:/Studia_mgr_BigDataAnalytics/Zajecia/1 semestr/Programming and Calssification/Laboratorium/Lista 2/Programming_and_Classification_List2/Explorations in Australia by John Forrest.txt')
# a)
words = nltk.word_tokenize(text['content'])
# b)
stop_words = set(stopwords.words('english')) 
filtered_sentence = [w for w in words if not w in stop_words]   
filtered_sentence = []   
for w in words: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
""" 
print(words) 
print('-----------------------------')
print(filtered_sentence) 
"""
# c)
ps = PorterStemmer() 

words_without_steam = []

for w in filtered_sentence: 
    if (w == ps.stem(w)):
        words_without_steam.append(w) 
"""
print(filtered_sentence)
print('-----------------------------')
print(words_without_steam)
"""
# d)

#count the frequency of the letters
freq_word={x:words_without_steam.count(x) for x in set(words_without_steam)}
#sort the data and reverse it
word_ranking=sorted(freq_word.items(),reverse=True,key=lambda x: x[1])

greater_100 = [x for x,y in word_ranking if y >= 100]

print(greater_100)