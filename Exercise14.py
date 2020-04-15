import nltk
#creating an empty dictionary
d = {}

#filling dictionary
d['Mateusz'] = 'Wroclaw'
d['Kamil'] = 'Warszawa'
d['Bartek'] = 'Poznan'
d['Kuba'] = 'Gdansk'

#listing dictionary
d_list = list(d.items())

#sort dictionary by adress using lambda function
print (sorted(d_list, key = lambda i: i[1]))