import pickle

with open("foodVectors.pickle", 'rb') as f:
    foodVecs = pickle.load(f)

with open("foodClusters.pickle", 'rb') as f:
    food_clusters = pickle.load(f)

print("Length of FoodVecs",len(foodVecs))
print("Length of food_clusters", len(food_clusters))

Clusters = dict()
DescriptionClusters = dict()

for i in range(len(food_clusters)):
    if(i%10000 == 0):
        print(i)
    if food_clusters[i] in Clusters :
        Clusters[food_clusters[i]].append(foodVecs[i])
    else:
        Clusters[food_clusters[i]] = [foodVecs[i]]
    if food_clusters[i] in DescriptionClusters:
        DescriptionClusters[food_clusters[i]].append(i) # saving index of associated to description in description.pickle
    else:
        DescriptionClusters[food_clusters[i]] = [i] # You can access associated description by desc[i] = String of descriptions

with open("ClusterDictionary.pickle",'wb') as cd:
    pickle.dump(Clusters, cd)

with open("DescriptionClusters.pickle", 'wb') as f:
    pickle.dump(DescriptionClusters, f)
