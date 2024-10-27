#!/usr/bin/env python3
import math
import numpy as np
import sklearn

person1 = [5, 2, 1, 0, 7, 10]
person2 = [10, 7, 9, 10, 1, 0]
person3 = [4, 3, 1, 0, 8, 5]
#person1 = [5, 2]
#person2 = [10, 7]

def euclidean_distance_calc(personA,personB):
    distance = 0
    for i in range(len(personA)):
        diffsq = (personA[i] - personB[i])**2
        distance += diffsq
    return math.sqrt(distance)

eucdistance = euclidean_distance_calc(person1,person3)
print(f'euc distance is {eucdistance}')


##Kmeans clustering
from sklearn.cluster import KMeans
data = np.array([person1,person2,person3])

#KMeans clustering with k=2
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(data) 
labels=kmeans.labels_
print("Cluster labels for each person:",labels)

#generate random people data to visualize kmeans clustering
np.random.seed(42) #initialize the random number generator

#parameters fo the dataset
num_people = 100
num_features = 6
feature_min = 1
feature_max = 10 #plused 1 because max is exclusive

random_people = np.random.randint(feature_min,feature_max+1,size=(num_people, num_features))
print(random_people)

#Kmeans clustering with random people included
