#food-description-vectors
import pickle;
from gensim.models import Word2Vec;
import numpy as np;

with open("description.pickle", 'rb') as f:
    foods = pickle.load(f)

model = Word2Vec.load('usda1.model')
foodvecs = []
i=0
for food in foods:
    i+=1
    vec = np.zeros(100)
    for token in food:
        vec += model.wv[token] # adding word_vectors of all the words in the food description sentence
    foodvecs.append(vec)
    if (i%10000 == 0):
        print(i)

with open('foodVectors.pickle','wb') as f:
    pickle.dump(foodvecs, f)

with open('foodVectors.pickle', 'rb') as f:
    saved = pickle.load(f)

print("Total description vectors are:",len(saved))
print(type(saved[1]),'\t', saved[1])
