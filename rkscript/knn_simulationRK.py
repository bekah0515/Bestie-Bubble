#!/Users/pfb2024/mamba/envs/bio/bin/python

import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

###Generate Random Sample Data:make 100 representative points with 5 features each
np.random.seed(42) #initialize the random number generator
representative_points = 1+4*np.random.rand(100, 5)
print(representative_points)

# #Test data for which we want to find the nearest neighbors by making 3 new points with 5 features each
# # new_points = 1+4*np.random.rand(3, 5)
# # # Assign names to the new points
# # new_point_names = ["New Point A", "New Point B", "New Point C"]
##input user data
user_dict = {'user1':{'agreeable':[5, 3, 4, 5],'Extraverted':[1, 2, 4], 'Openness':[1, 2, 4], 'Conscientiousness':[5, 4, 4], 'Neuroticism':[2, 2, 4]}, 'user2':{'agreeable':[1, 3, 2, 1],'Extraverted':[5, 4, 3, 3], 'Openness':[5, 4, 3, 2], 'Conscientiousness':[1, 2, 4], 'Neuroticism':[1, 2, 0]}}

#Calculate the average for each feature of each user
averages_user = {}
for user, traits in user_dict.items():
    averages_user[user] = {}
    for trait, scores in traits.items():
        avg_score = sum(scores) / len(scores)  # Calculate the average score
        averages_user[user][trait] = avg_score

#convert averages to array of lists per value and use as our input
new_points = np.array([list(features.values()) for features in averages_user.values()])
print(new_points)

new_point_names = list(averages_user.keys())
print(new_point_names)

#Initialize the NearestNeighbors model to find the 10 nearest neighbors
n_neighbors = 10
nearest_neighbors = NearestNeighbors(n_neighbors=n_neighbors, algorithm='auto')

#Fit the model on the representative points
nearest_neighbors.fit(representative_points)

#Find the 10 nearest neighbors for each new point
distances, indices = nearest_neighbors.kneighbors(new_points)

#Output the results
for i, (dists, idxs) in enumerate(zip(distances, indices)):
    print(f"New Point {i+1}:")
    print("Indices of Nearest Neighbors:", idxs)
    print("Distances to Nearest Neighbors:", dists)
    print()


#Reduce dimensions to 2D for visualization using PCA
pca = PCA(n_components=2)
rep_points_2d = pca.fit_transform(representative_points)
new_points_2d = pca.transform(new_points)

#Plot representative points
plt.figure(figsize=(10, 6))
plt.scatter(rep_points_2d[:, 0], rep_points_2d[:, 1], color='black', label='Representative Points', alpha=0.6)

#Plot new points
plt.scatter(new_points_2d[:, 0], new_points_2d[:, 1], color='red', label='New Points', marker='X', s=100)

#Draw lines to the 10 nearest neighbors for each new point
for i, (dists, idxs) in enumerate(zip(distances, indices)):
    for idx in idxs:
        plt.plot([new_points_2d[i, 0], rep_points_2d[idx, 0]],
                 [new_points_2d[i, 1], rep_points_2d[idx, 1]], 'k--', linewidth=0.5)

# Annotate each new point with its name
for i, name in enumerate(new_point_names):
    plt.text(new_points_2d[i, 0] + 0.02, new_points_2d[i, 1] + 0.02, name, color='red', fontsize=10)

plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend()
plt.title("2D Visualization of New Points and their Nearest Neighbors")
plt.show()