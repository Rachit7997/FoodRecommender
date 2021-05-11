#Check the centroids
import pickle;
import numpy as np;
#import math;
from sklearn.cluster import KMeans;

with open("foodVectors.pickle", 'rb') as f:
    foodVecs = pickle.load(f)

with open("description.pickle", 'rb') as f:
    foods = pickle.load(f)

print("The food in total:",len(foodVecs))
print("demo:",foodVecs[1])
kmeans = KMeans(n_clusters = 100, random_state = 0)
vectors = np.array(foodVecs); #making 2D numpy array

clustered = kmeans.fit_predict(vectors)

tags = enumerate(clustered)

centroids = kmeans.cluster_centers_

with open("foodClusters.pickle","wb") as f:
    pickle.dump(clustered, f)

with open("foodCentroids.pickle", 'wb') as f:
    pickle.dump(centroids, f)
