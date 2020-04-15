import nltk

#import all books from nltk.books
from nltk.book import *
#import text 6
text_mp=[x.lower() for x in text6]
freq_mp={x:text_mp.count(x) for x in set(text_mp)}
#import text 7
text_wsj=[x.lower() for x in text7]
freq_wsj={x:text_wsj.count(x) for x in set(text_wsj)}
#sort text 6
word_r_mp=sorted(freq_mp.items(), reverse=True, key=lambda x : x[1])
#sort text 7
word_r_wsj=sorted(freq_wsj.items(), reverse=True, key=lambda x : x[1])
# eliminating stopwords
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))

for(w,c) in word_r_mp:
    if w in stop_words:
        word_r_mp.remove((w,c))
for(w,c) in word_r_wsj:
    if w in stop_words:
        word_r_wsj.remove((w,c))

#create dictionary from text 6 and 7
mp_dict=dict(word_r_mp)
wsj_dict=dict(word_r_wsj)

# checking how many times the word 'knight' appears
print(mp_dict['knight'])
#84
print(wsj_dict['knight'])
#1