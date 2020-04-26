# Programming_and_Classification_List2
> I will show a few examples of result i got from the exercises.

## Exercise 11
- Use https://www.wordclouds.com/to  build  a  word  cloud  for  your  favouritebook.

**So i choosed one random book, and it was Winnie: The Pooh.**

> Steps i made:
- reading the winnie pooh pdf using 'parser.from_file()' method
```python
text = parser.from_file("D:/Studia_mgr_BigDataAnalytics/Zajecia/1 semestr/Programming and Calssification/Laboratorium/Lista 2/Programming_and_Classification_List2/winnie-the-pooh.pdf")
```
- tokenize the data using 'nltk.tokenize()' method
```python
text = nltk.word_tokenize(text['content'])
```
- i made the letters to as a lower text using 'lower()' method
```python
text_wp=[x.lower() for x in text]
```
- i counted the frequency of the letters using 'count()' method
```python
freq_wp={x:text_wp.count(x) for x in set(text_wp)}
```
- i sorted the data usig 'sorting()' method and using lambda function
```python
word_ranking_wp=sorted(freq_wp.items(),reverse=True,key=lambda x: x[1])
```
- i deleted stopwords
```python
stop_words = set(stopwords.words('english'))
for (w,c) in word_ranking_wp:
    if w in stop_words:
        word_ranking_wp.remove((w,c))
```
- and made a dictionary
```python
wp_map=dict(word_ranking_wp)
```
- then i saved the data using 'DaataFrame' method to csv and plotted word cloud using the upper link
```python
pd.DataFrame(word_ranking_wp).to_csv('winnie_pooh.csv', index=False)
```

## Results

[![Results](https://raw.githubusercontent.com/matetuh/Programming_and_Classification_List2/master/wordcloud.jpg)]()




