 #Analysis description
import pickle;
import numpy as np;
import pandas as pd;

from gensim.models import Word2Vec;
from gensim.test.utils import get_tmpfile;



food_df = pd.read_csv(r'./data/FoodData_Central_csv_2019-12-17/food.csv');
food = food_df.values; #It returns a 2D numpy array
print(food.shape)
print(food.dtype);#Doesn't matter at all

with open('description.pickle', 'rb') as f:
    saved = pickle.load(f)

print(len(saved))
print(type(saved))
print(saved[1])

path = get_tmpfile("usda1.model")
print("Training Word2Vec model by list of tokenized food-description")

#trainning the model by my 2D array
model = Word2Vec(saved, size=100, window=5, min_count=1, workers=4)

model.save("usda1.model")

print("Vactore of banana", model.wv['banana'])
