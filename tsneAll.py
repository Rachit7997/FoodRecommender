import numpy as np
import pickle
from sklearn.manifold import TSNE

with open('ClusterDictionary.pickle', 'rb') as f:
    c_dict = pickle.load(f)

print("c_dict is loaded, Length:",len(c_dict))

for n in range(1,6):
    coordinates = np.array(c_dict[(n-1)*10])
    lengths = [len(c_dict[(n-1)*10])]
    for i in range(((n-1)*10)+1, n*10):
        lengths.append(len(c_dict[i]))
        coordinates = np.concatenate((coordinates, np.array(c_dict[i])), axis=0)
    print(f"{n} coordinates.shape {coordinates.shape}")
    coordinates_embedded = TSNE(n_components=2).fit_transform(coordinates) #tsne embedding
    print(f"{n} coordinates_embedded.shape: {coordinates_embedded.shape}")
    list1 = coordinates_embedded.tolist();
    with open(f"tsne_embed{n}.pickle1",'wb') as f:
        pickle.dump(list1, f)
    with open(f"tsne_lengths{n}.pickle1",'wb') as f:
        pickle.dump(lengths, f)
    print(f"The files are seved: {n}")
