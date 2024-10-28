#!/Users/pfb2024/mamba/envs/bio/bin/python3
import sys, os
def nn_algorithm(repfile,inputfile):
    import pandas as pd
    from sklearn.neighbors import NearestNeighbors
    import numpy as np
    import matplotlib.pyplot as plt
    import sys
    from InputToDatabase import FileToDict
    ############################

    ##Generate representative points database##
    rep_dict = FileToDict(repfile)
    #print(rep_dict)
    averages = {}
    for user, traits in rep_dict.items():
        averages[user] = {}
        for trait, scores in traits.items():
            scores = [int(item) for item in scores]
            avg_score = sum(scores) / len(scores) 
            # Calculate the average score
            averages[user][trait] = avg_score

    #convert averages to array of lists per value and use as our input
    representative_points = np.array([list(features.values()) for features in averages.values()])
    #print(representative_points)
    representative_points_names = list(averages.keys())
    #print(representative_points_names)

    ##############################
    #user_dict = {'John Doe':{'agreeable':[5, 3, 4, 5],'Extraverted':[1, 2, 4], 'Openness':[1, 2, 4], 'Conscientiousness':[5, 4, 4], 'Neuroticism':[2, 2, 4]}, 'Mike Micky':{'agreeable':[1, 3, 2, 1],'Extraverted':[5, 4, 3, 3], 'Openness':[5, 4, 3, 2], 'Conscientiousness':[1, 2, 4], 'Neuroticism':[1, 2, 0]}}
    ##import user data

    user_dict = FileToDict(inputfile)
    #Calculate the average for each feature of each user
    averages_user = {}
    for user, traits in user_dict.items():
        averages_user[user] = {}
        for trait, scores in traits.items():
            scores = [int(item) for item in scores]
            avg_score = sum(scores) / len(scores) 
            # Calculate the average score
            averages_user[user][trait] = avg_score

    #convert averages to array of lists per value and use as our input
    new_points = np.array([list(features.values()) for features in averages_user.values()])
    #print(new_points)

    new_point_names = list(averages_user.keys())
    #print(f'new point names:{new_point_names}')

    ##############################
    ###Run NearestNeighbors function
    #Initialize the NearestNeighbors model to find the 3 nearest neighbors
    n_neighbors = 3
    nearest_neighbors = NearestNeighbors(n_neighbors=n_neighbors, algorithm='auto')

    #Fit the model on the representative points
    nearest_neighbors.fit(representative_points)

    #Find the 10 nearest neighbors for each new point
    distances, indices = nearest_neighbors.kneighbors(new_points)

    #Output the results
    for i, (dists, idxs) in enumerate(zip(distances, indices)):
        match_name_list = [representative_points_names[idx] for idx in idxs]
        user_name = new_point_names[i]
        print(f"Name:{user_name}")
        print("Indices of Nearest Neighbors:", idxs)
        print("Names of top 3 matches:", match_name_list)
        print("Distances to Nearest Neighbors:", dists)

    result_dict = {}
    for i, (new_point, dists, idxs) in enumerate(zip(new_point_names, distances, indices)):
        index_to_name_list = [representative_points_names[idx] for idx in idxs]
        inner_dict = {neighbor: dist for neighbor, dist in zip(index_to_name_list, dists)}
        result_dict[new_point] = inner_dict

    neighbor_keys_array = [list(neighbors.keys()) for neighbors in result_dict.values()]

    from sklearn.decomposition import PCA
    ###Reduce dimensions to 2D for visualization using PCA###
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
            plt.plot([new_points_2d[i, 0], rep_points_2d[idx, 0]], [new_points_2d[i, 1], rep_points_2d[idx, 1]], 'k--', linewidth=0.5)

    # Annotate each new point with its name
    for i, name in enumerate(new_point_names):
        plt.text(new_points_2d[i, 0] + 0.02, new_points_2d[i, 1] + 0.02, name, color='red', fontsize=10)

    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.legend()
    plt.title("2D Visualization of New Points and their Nearest Neighbors")
    #save the plot
    plt.savefig("./nearest_neighbor_plot.png", format = 'png', dpi = 300)
    #plt.show()
    #return_stuff=[result_dict,neighbor_keys_array]
    return result_dict, neighbor_keys_array


# repfile = sys.argv[1]
# inputfile = sys.argv[2]
# result_dict, list_of_matches = nn_algorithm(repfile, inputfile)
# print("result_dict:", result_dict)
# print("list of matches:", list_of_matches)