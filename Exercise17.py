import nltk

#import all books from nltk.books
from nltk.book import *
#import text 1
text_1=[x.lower() for x in text1]
#import text 2
text_2=[x.lower() for x in text2]
#import text 3
text_3=[x.lower() for x in text3]
#import text 4
text_4=[x.lower() for x in text4]
#sort text 5
text_5=[x.lower() for x in text5]
#import text 6
text_6=[x.lower() for x in text6]
#sort text 7
text_7=[x.lower() for x in text7]
#import text 8
text_8=[x.lower() for x in text8]
#import text 9
text_9=[x.lower() for x in text9]

#import stopwords
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))

for w in text_1:
    if w in stop_words:
        text_1.remove(w)
for w in text_2:
    if w in stop_words:
        text_2.remove(w)
for w in text_3:
    if w in stop_words:
        text_3.remove(w)
for w in text_4:
    if w in stop_words:
        text_4.remove(w)
for w in text_5:
    if w in stop_words:
        text_5.remove(w)
for w in text_6:
    if w in stop_words:
        text_6.remove(w)
for w in text_7:
    if w in stop_words:
        text_7.remove(w)
for w in text_8:
    if w in stop_words:
        text_8.remove(w)
for w in text_9:
    if w in stop_words:
        text_9.remove(w)
        
the_same_words = []
#append the same words if they are similar
for w in text_1:
    if w in text_2 and text_3 and text_4 and text_5 and text_6 and text_7 and text_8 and text_9 :
        the_same_words.append(w)


print(the_same_words)