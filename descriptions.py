#Doc2Vec
import spacy
import gensim
import pandas as pd
import numpy as np
import pickle

nlp = spacy.load("en_core_web_sm")

#change the path accoording to the address of food.csv file
food_df = pd.read_csv(r'./data/FoodData_Central_csv_2019-12-17/food.csv')
food = food_df.values
print (len(food))
data = []
desc = []
k=0
print(food[1,2])
for i in food[:,2]:
    l = []
    if k%10000 == 0:
        print(k)
    for j in i:
        if j != '\\' and j != '.':
            l.append(j)
    desc.append(''.join(l))     #l doesn't contain \\.
    k+=1

print("Preprocessing is complete.\n")
print(desc[1])

POS = ['CONJ', 'VERB', 'ADJ', 'NOUN', 'PROPN', 'PART', 'ADV'] # exclusing stopping words
k=0
for s in desc:
    if k%10000 == 0:
        print(k)
    data.append([token.text.lower() for token in nlp(s) if token.pos_ in POS])
    k+=1
print(data[:10])

with open('description.pickle','wb') as f:
    pickle.dump(data,f)

with open('description.pickle','rb') as f:
    saved = pickle.load(f)

print("Length of saved description:",len(saved))
print(saved[1])
