import numpy as np
import pickle
import matplotlib.pyplot as plt

colors = ["#0008ff", "#00ff33", "#00fff7", "#f6ff00", "#ff8800", "#ff0000", "#ff006f", "#ff00f2", "#8000ff", "#008cff"]

clgrp1 = ['Mixed Fruit variety', 'cookies and baked snacks', 'Edible Oils', 'Fresh fried and roasted foods', 'water and beverages',
            'grains and bars', 'fast foods', 'dry fruits and bars', 'frozen Red meats', 'mexican snacks']

clgrp2 = ['cooked meats', 'italian fast foods', 'sweets and snacks', 'cakes and brownies', 'dairy snacks', 'roasted dry fruits',
            'variety chocolates', 'mixed fruits and chocolates', 'fresh chopped meats', 'variety cheeses']

clgrp3 = ['grills', 'variety noodles', 'Non veg dishes', 'fruit juices', 'mouth fresheners', 'Natural flavoured bars and coockies',
            'egg foods', 'veg grills', 'variety beans', 'Sauces']

clgrp4 = ['variety mustered', 'whole seeds', 'creams', 'cereals', 'Red meat meals', 'variety yogurts', 'granola bars', 'gravys and purees',
            'fruit candies', 'italian dishes']

clgrp5 = ['chicken snacks', 'chunks', 'milk products', 'fruit cereals', 'meat soups', 'low fat and dairy free', 'fruits and veges', 'Seasoning',
            'natural fruit juices', 'ice creams']


"""
tsne_embed1.pickle -> tsne_lengths1.pickle
tsne_embed2.pickle -> tsne_lengths2.pickle
tsne_embed3.pickle -> tsne_lengths3.pickle
tsne_embed4.pickle -> tsne_lengths4.pickle
tsne_embed5.pickle -> tsne_lengths5.pickle
"""

with open('tsne_embed3.pickle','rb') as f: #replace the file name from the list above
    l = pickle.load(f)
with open('tsne_lengths3.pickle', 'rb') as f: #choose an appropriate lengths from the list above
    lens = pickle.load(f) #lens is a short form of Lengths

x, y = zip(*l)
total = 0
fig, ax = plt.subplots()
for i in range(10):
    ax.scatter(x[ total : (total+lens[i]) ], y[ total : (total+lens[i]) ],color=colors[i], label=clgrp3[i],s=35)
    total+=lens[i]
ax.legend()
plt.show()
