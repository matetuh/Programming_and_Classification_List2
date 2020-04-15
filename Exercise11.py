#importing libraries
import nltk
from nltk.corpus import stopwords
import pandas as pd
from tika import parser

#reading the winnie pooh pdf
text = parser.from_file("D:/Studia_mgr_BigDataAnalytics/Zajecia/1 semestr/Programming and Calssification/Laboratorium/Lista 2/Programming_and_Classification_List2/winnie-the-pooh.pdf")
#toknize the data
text = nltk.word_tokenize(text['content'])
#make the letters lower text
text_wp=[x.lower() for x in text]
#count the frequency of the letters
freq_wp={x:text_wp.count(x) for x in set(text_wp)}
#sort the data and reverse it
word_ranking_wp=sorted(freq_wp.items(),reverse=True,key=lambda x: x[1])
#importing stopwords
stop_words = set(stopwords.words('english'))
#deleting stopwords
for (w,c) in word_ranking_wp:
    if w in stop_words:
        word_ranking_wp.remove((w,c))

wp_map=dict(word_ranking_wp)
#saving the data to csv and than making the word weight graphic
pd.DataFrame(word_ranking_wp).to_csv('winnie_pooh.csv', index=False)