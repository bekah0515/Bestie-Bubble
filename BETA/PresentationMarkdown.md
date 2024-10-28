# PFB 2024 Project: Bestie Bubble

**Isobel Fetter, Harshad Ingle, Bekah Kim, Konstantin Queitsch, Lola Takhirov | Riley Kellermeyer**

## Project Goals:
* Build a GUI to uptake new user information and inputs. 
* Read in 1) numerical survey 2) categorical survey data for users into complex data structures in Python.
* Leverage K-Nearest Neighbors Algorithm to determine top matches based on similarity and plot clusters.
* Calculate Simularity Scores using Euclidean Distances and plot simuleratiy.
* Extend GUI for visual disply of plotted outputs for BestieBubbles&trade;.

## Building the GUI 
#!/Users/pfb2024/mamba/envs/projects/bin/python3

#This is the home page 
import ttkbootstrap as ttkb
import tkinter as tk
from PIL import Image, ImageTk
import csv
import os

current_question = 0
answers = ""

def function1():
    all_lines = []
    with open("personality_data_info.txt", 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            line = line.strip().split("\t")
            processed_line = '\t'.join(line[1:])
            all_lines.append(processed_line)
    return(all_lines)

questions = function1()

#function to create a new window 
def open_new_window():
    if current_question < len(questions):
        display_question()
    else:
        end_quiz()
        export_to_csv(user_name)
       
        # match_page()
# def open_new_window(question_number):
#    for widget in overlay_frame.winfo_children():
#         widget.destroy()
#    second_page()

def display_question():
    question_text = questions[current_question]
    
    # Clear the previous widgets
    for widget in overlay_frame.winfo_children():
        widget.destroy()

    # Display the current question
    label1 = tk.Label(overlay_frame, text=question_text, font=("Arial", 40, "bold"), bg='light sea green')
    label1.pack(pady=20)
    label2 = tk.Label(overlay_frame, text = "Please answer the question with an integer value. 1 corresponds to least agree, 3 is neutral, and 5 is most agree.", font=("Arial", 30), bg='light sea green')
    label2.pack(pady=20)

    entry1 = tk.Entry(overlay_frame, font=font, justify = "center")
    entry1.pack(pady=20)

    button1 = tk.Button(overlay_frame, text="Next question!", font=font, bg='light sea green',
                        command=lambda: next_question(entry1.get()))  # Capture user input
    button1.pack(pady=20)

def next_question(user_answer):
    global current_question, answers
    answers += user_answer + ","  # Store the user's answer
    current_question += 1  # Move to the next question
    open_new_window()

def end_quiz():
    global current_question, answers
    for widget in overlay_frame.winfo_children():
        widget.destroy()
    label_end = tk.Label(overlay_frame, text="Thank you for participating!", font=("Arial", 40, "bold"), bg='light sea green')
    label_end.pack(pady=20)
    button10 = tk.Button(overlay_frame, text = "Click here to get your match!", command = on_button2_click, font = font)
    button10.pack()
    export_to_csv(user_name)

def export_to_csv(user_name):
    # Specify the file path (you can change this to your desired location)
    file_path = os.path.expanduser(f'./{user_name}_answers.csv')
    print(file_path)
    # Write answers to CSV
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file) 
        writer.writerow(answers.split(','))  # Write the collected answers


#Make a window and add the image as the background 
parent = tk.Tk()
parent.title("Image in Tkinter")
parent.attributes("-fullscreen", True) 
image = Image.open("Bestie_artwork1.png")
image = image.resize((parent.winfo_screenwidth(), parent.winfo_screenheight()))
image = ImageTk.PhotoImage(image)
image_label = tk.Label(parent, image = image)

#Make it so that the widgets can be layered on 
overlay_frame = tk.Frame(parent, bg='light sea green', bd=0)
overlay_frame.place(relx=0.5, rely=0.2, anchor='center')

#Change the font 
font_size = 40
font = ("Arial", font_size)

#To get the user input of names this is the function
def on_button1_click():
    global user_name, answers
    user_name = entry.get()
    answers += user_name + ","
    label3 = tk.Label(overlay_frame, text = f'Welcome {user_name}!', font = font, bg='light sea green')
    label3.pack()
    overlay_frame.after(1000, open_new_window)

def on_button2_click():
    open_match()

def open_match():
    # Clear previous widgets
    for widget in overlay_frame.winfo_children():
        widget.destroy()
    info_frame = tk.Frame(overlay_frame, bg='light sea green')
    info_frame.pack(side="top", pady=(700, 20))  # Add padding to move it down

    label_match = tk.Label(info_frame, text="Your top two matches are: April Tran and Grace Watson", font=("Arial", 40, "bold"), bg='light sea green')
    label_match.pack(pady=10)

    button11 = tk.Button(info_frame, text="Click here to get more information!", font=font, command = open_match2)
    button11.pack(pady = 10)

    image_frame2 = tk.Frame(overlay_frame, bg='light sea green')
    image_frame2.pack(side="top", fill="x", pady = 20)  # Fill the width at the bottom

    image6 = Image.open("Simon_bestie_matches.png")
    image6 = image6.resize((1100, 800))
    image6_tk = ImageTk.PhotoImage(image6)
    image_label6 = tk.Label(image_frame2, image=image6_tk, bg='light sea green')
    image_label6.image = image6_tk  # Keep a reference
    image_label6.pack()



      # Fill the width at the bottom
    

def open_match2():
    for widget in overlay_frame.winfo_children():
        widget.destroy()

    # Adjust the padding for image_frame3
    image_frame3 = tk.Frame(overlay_frame, bg='light sea green')
    image_frame3.pack(side="top", pady=(700, 20))  # Add more top padding

    # Load images 3, 4, and 5
    image3 = Image.open("DavidDukeandAprilTran.png")
    image4 = Image.open("DavidDukeandGraceWatson.png")
    # image5 = Image.open("SMOLLYandAmanda Herrera MD.png")
    image3 = image3.resize((500, 500))
    image4 = image4.resize((500, 500))
    # image5 = image5.resize((500, 500))

    # Create PhotoImage references
    image3_tk = ImageTk.PhotoImage(image3)
    image4_tk = ImageTk.PhotoImage(image4)
    # image5_tk = ImageTk.PhotoImage(image5)

    # Create labels for images and grid them
    image_label3 = tk.Label(image_frame3, image=image3_tk, bg='light sea green')
    image_label3.image = image3_tk  # Keep a reference
    image_label3.pack(side="left", padx=10, pady=10)

    image_label4 = tk.Label(image_frame3, image=image4_tk, bg='light sea green')
    image_label4.image = image4_tk  # Keep a reference
    image_label4.pack(side="left", padx=10, pady=10)

    # image_label5 = tk.Label(image_frame3, image=image5_tk, bg='light sea green')
    # image_label5.image = image5_tk  # Keep a reference
    # image_label5.pack(side="left", padx=10, pady=10)

    # Create a frame for image 7
    info_frame3 = tk.Frame(overlay_frame, bg='light sea green')
    info_frame3.pack(side="top", pady=(20, 20))

    image7 = Image.open("nearest_neighbor_plot.png")
    image7 = image7.resize((900, 500))
    image7_tk = ImageTk.PhotoImage(image7)

    image_label7 = tk.Label(info_frame3, image=image7_tk, bg='light sea green')
    image_label7.image = image7_tk  # Keep a reference
    image_label7.pack(pady=10)


#Add the other widgets 
entry = tk.Entry(overlay_frame, font = font, justify = "center")
button = tk.Button(overlay_frame, text = "Click here to begin!", command = on_button1_click, font = font)
#button2 = tk.Button(overlay_frame, text = "Click me to begin!", command = open_new_window, font = font)
label = tk.Label(overlay_frame, text = "Welcome! You are on the right path to finding your bestie! ", font = ("Arial", 40, "bold"), bg='light sea green')
label2 = tk.Label(overlay_frame, text = "Please enter your name in the box", font = font, bg='light sea green')

#Push the widgets into the frame 
label.pack()
label2.pack()   
entry.pack(pady = 20)
button.pack(pady = 20)
#button2.pack(pady = 20)
image_label.pack()
parent.mainloop()

print(answers)

## Reading in Numerical Data
### Reading in the Test Data

#### NamedSubInput.py
Generate Fake Names and add them as the first column for the public data set we found. Not technically part of the pipeline, but a very fun package! 
```
import pandas as pd
from faker import Faker

#Generate 1000 fake names
fake = Faker()
random_names = [fake.name() for _ in range(1000)]
# Read the existing CSV file
df = pd.read_csv('/Users/pfb2024/BestieBubble2/Bestie-Bubble/sub.trimmed.file.csv')
# Insert an empty column at the first position
df.insert(0, 'Name', '')
# Populate the 'Name' column with random names
df['Name'] = random_names[:len(df)]
# Save the updated DataFrame to a new CSV file
df.to_csv('named.sub.trimmed.csv', index=False)
print("Updated CSV file saved as 'updated_file.csv'")
```
#Dictionary for user input
import json

def function1():

    dict1 = {}
    global_dict = {}
    output_file = 'output_1.txt'
    with open("personality_data_info.txt", 'r') as input_file, open(output_file,"w") as output:
        print('personality_data_info.txt')
        lines = input_file.readlines()
        for line in lines:
            key, value = line.strip().split('\t')
            big_key = key[0:3]
            #print(big_key)
            if big_key not in global_dict:
                global_dict[big_key] = {}
                dict1[key.strip()] = value.strip()
            if big_key in global_dict:
                global_dict[big_key][key] = value.strip()
            #print(global_dict,"@@##$$")
        #print(f'writing to {output_file}')
        output.write(json.dumps(global_dict))
    return(global_dict)

#test_dict = global_dict[big_key]
#print(test_dict)
def function2(username):
    global_dict = function1()
    user_data = {}
    for category in global_dict:
        user_data[category] = {}
        for key in global_dict[category]:
            user_data[category][key] = []
        #if username in key:
            #user_data[key] = value
    print(f"{username}:")
    #print(json.dumps(user_data))
    print(user_data)
   
def main():
    username = input('Enter your name')
    function2(username)

if __name__=='__main__':
    main() 

#### InputToDict.py
This reads in our test data set and breaks it up into a dictionary.

{User : {Attribute : [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10], Attr...}, ...}

```
import csv

def FileToDict(filename):
    user_dict = {}
    with open(filename, mode='r') as INPUT:
        
        csv_reader = csv.reader(INPUT)
        for row in csv_reader:
            user_name = row[0]
            att_dict = {
                'Agreeableness': row[1:11],
                'Extroverted': row[11:21],
                'Openness': row[21:31],
                'Conscientiousness': row[31:41],
                'Neuroticism': row[41:51]
            }
            user_dict[user_name] = att_dict
            
        return user_dict


# Main execution block
if __name__ == "__main__":
    # Example usage
    import json
    file_path = '../BETA/30subs.named.csv'  
    user_dict = FileToDict(file_path)
    with open('30UserSubbed.txt', 'w') as file:
        json.dump(user_dict, file)
```


### Reading in User Input as a New Line


## Reading in Categorical Data

## Matching based on Categorical Data
We also wanted to create a method for matching people to labs/PIs, but the matching variables would be categorical and not numerical. For example:
    Lab location: North East, South, Midwest, West
    Model organism: Human, Mouse, Fly, Worm, Yeast

We could convert the data to numbers, but that could make some things seem more similar than others (based on the numbers assigned to each option), when in reality they are equally dissimilar. So how can we find similarity between categorical data?

### Categorical Similarity Algorithms
#### Jaccard Distance
The Jaccard distance between two sets of values (A, B) is defined as:
    overlap of A and B / sum of A and B

As two sets of values have more in common, the overlap will increase and the sum will decrease. If A = B, the Jaccard distance = 1, and if A and B have no values in common, the Jaccard distance = 0.

```
jaccard_dict = {} #calulating Jaccard distance: (overlap of A and B) / (sum of A and B)
for name in data_dict:
    data_set = set(data_dict[name].values())
    set_overlap = data_set & user_set
    set_sum = data_set | user_set
    jaccard = len(set_overlap) / len(set_sum)
    jaccard_dict[name] = jaccard
```

#### Gower Similarity
The Gower similarity between two sets of values (A, B) is defined as:
    sum of [if value(A)=value(B), 1, if value(A)!=value(B)] over all variables / # of variables

As two sets of values have more in common, there will be more 1s and thus the sum will increase. We could also add an additional value, where if value(A) is similar but not identical to value(B), we could add 0.5 as an intermediate value between 0 for no match and 1 for identical. 

However, defining similar values is a future endeavor, and we just used 1 for match and 0 for no match.

```
gower_dict = {} #calculating Gower similarity: sum of (0 if not match, 1 if match) across variables / # of variables
for name in data_dict:
    gower_sum = 0
    for key in user_data:
        if user_data[key] == data_dict[name][key]: #0.5 if similar but not identical? Would need to define similar things
            gower_sum +=1
    gower = gower_sum / len(user_data)
    gower_dict[name] = gower
```

These functions are dependent on a database of potential matches. This could eventually be real PIs, but for now it is randomly generated data.

```
#!/usr/bin/env python3

import random
location_list = ['North East', 'South', 'Midwest', 'West']
dept_list = ['Molecular Biology', 'Chemistry', 'Neuroscience', 'Ecology', 'Bioinformatics']
style_list = ['Wet', 'Dry', 'Both']
interaction_list = ['Lots', 'Some', 'Minimal']
org_list = ['Human', 'Mouse', 'Arabidopsis', 'Fly', 'Worm', 'Yeast', 'Zebrafish', 'Non-Model Organism', 'None']
tech_list = ['Sequencing', 'Microscopy', 'Flow Cytometry', 'Western Blot', 'Coding']

name_list = []
with open('science_database.txt', 'r') as input_file:
    for line in input_file:
        line = line.rstrip()
        name_list.append(line)

data_dict = {}
for name in name_list:
    data_dict[name] = {}
    data_dict[name]['location'] = random.choice(location_list)
    data_dict[name]['department'] = random.choice(dept_list)
    data_dict[name]['style'] = random.choice(style_list)
    data_dict[name]['interaction'] = random.choice(interaction_list)
    data_dict[name]['organism'] = random.choice(org_list)
    data_dict[name]['technique'] = random.choice(tech_list)

output_file = open('science_database.txt', 'w')
for name in data_dict:
    output_file.write(f'{name}\t{data_dict[name]['location']}\t{data_dict[name]['department']}\t{data_dict[name]['style']}\t{data_dict[name]['interaction']}\t{data_dict[name]['organism']}\t{data_dict[name]['technique']}\n')

print('Database generated and written to science_database.txt')
```

### Getting User Input
We limit the user input to a predefined list for each question to ensure there are some matches with the database. Allowing free input of categorical data would require a machine learning approach to group similar inputs together.

```
def science_quiz():
    username = input('Enter your name:\n')
    user_dict = {}

    print('Where would you like to work?')
    location_list = ['North East', 'South', 'Midwest', 'West']
    location = input(f'Choose one: {location_list}\n').title()
    if location not in location_list:
        print(f'Location not recognized, please choose from the list')
        location = input(f'Choose one: {location_list}\n')
    user_dict['location'] = location

    print('What department are you looking for?')
    dept_list = ['Molecular Biology', 'Chemistry', 'Neuroscience', 'Ecology', 'Bioinformatics']
    department = input(f'Choose one: {dept_list}\n').title()
    if department not in dept_list:
        print(f'Department not recognized, please choose from the list')
        department = input(f'Choose one: {dept_list}\n')
    user_dict['department'] = department

    output_file = open('user_science_answers.txt', 'w')
    output_file.write(f'{username}\t')
    for question in user_dict:
        output_file.write(f'{user_dict[question]}\t')
```
### Graphical Representation of Matches
Finally, we use the calculated distances (Gower and Jaccard) to visualize the best matches to the user input. The below code is simplified for readability, the code called in the final script includes adjustments for text overlap. This code can also be used to visualize the calculated Euclidean distances in the personality matching program.

```
import pandas, os
import plotly.express as px

def similarity_grapher():

    similarity_dict = {}
    jaccard_similarity = {}
    with open('categorical_similarity.txt', 'r') as read_file:
        for line in read_file:
            line = line.rstrip()
            [name, jaccard, gower] = line.split('\t')
            similarity_dict[name] = {}
            similarity_dict[name]['Jaccard'] = float(jaccard)
            similarity_dict[name]['Gower'] = float(gower)
            jaccard_similarity[name] = float(jaccard)

    sorted_sims = sorted(jaccard_similarity, key=jaccard_similarity.get, reverse=True)

    sorted_dict = {}
    for name in sorted_sims:
        sorted_dict[name] = {}
        sorted_dict[name]['Jaccard'] = similarity_dict[name]['Jaccard']
        sorted_dict[name]['Gower'] = similarity_dict[name]['Gower']


    colors = ['black'] * len(sorted_dict)
    colors[0] = 'magenta'
    colors[1] = '#FFD700'
    colors[2] = '#C0C0C0'
    colors[3] = '#CD7F32'
    colors[len(sorted_dict)-1] = "#8FC554"

    markers = ['circle'] * len(sorted_dict)
    markers[0] = 'star'

    sizes = [5] * len(sorted_dict)
    sizes[0] = 20

    names = [''] * len(sorted_dict)
    names[0] = sorted_sims[0] + " 🦄"
    names[1] = sorted_sims[1] + " 🥇"
    names[2] = sorted_sims[2] + " 🥈"
    names[3] = sorted_sims[3] + " 🥉"
    names[len(sorted_dict) -1] = sorted_sims[len(sorted_dict)-1] + " 🐸"

    text_position = ['top center'] * len(sorted_dict)
    text_position[1] = 'bottom center'
    text_position[3] = 'bottom center'

    column_label = ['Jaccard','Gower']
    similarities = pandas.DataFrame.from_dict(sorted_dict, orient='index', columns=column_label)
    similarities['color'] = colors
    similarities['marker'] = markers
    similarities['y-axis'] = 0
    similarities['size'] = sizes
    similarities['name'] = names
    similarities['textposition'] = text_position

    if not os.path.exists('images'):
        os.mkdir('images')


    fig = px.scatter(similarities, x='Gower', y='y-axis', color='color', 
                    color_discrete_map='identity', symbol='marker', 
                    symbol_map='identity', size='size')
    fig.update_yaxes(visible=False)
    for distance in sorted_sims:
        if names[sorted_sims.index(distance)] != "":
            fig.add_annotation(x=sorted_dict[distance]['Gower'],y=0, 
                            text=names[sorted_sims.index(distance)], 
                            showarrow=True, arrowhead=1, textangle=75)  
    fig.write_image(f"images/{sorted_sims[0]}_gower_matches.png", scale=2)
```
### Final Script
The following script calls on the 3 functions defined in different scripts. The user answers a short quiz on the command line, then the match images are saved to a directory named "images" in the current directory. Eventually this could be part of the GUI, where you initially answer if you're looking for a personality match (numerical data) or lab match (categorical data).

```
#!/usr/bin/env python3

import pandas, os
import plotly.express as px
from science_match_quiz import science_quiz
from categorical_similarity import similarity_calc
from euclid_grapher_science import similarity_grapher

science_quiz()
similarity_calc()
similarity_grapher()
```


## K-Nearest Neighbors Algorithm on Numerical Data
The K-Nearest Neighbors algorithm is a powerful tool used in machine learning and pattern recognition to gorup or classify data. Given an item, this algorithm looks for the most similar items it has seen before and makes predictions or classifications based on them. Many social media and music platforms, such as Spotify, uses this algorithm to suggest new music you may enjoy!

1. For each user we need a list of values corresponding to each attribute (e.g. {user:[a,b,c,d,e]})
    a. pull answers from input file/dictionary per person
    b. average the scores for each attribute
    c. assign username as key and a list of these scores as value.
2. Do the same for my representative data (database from which I want to find a match) as well. (e.g. {'name':[a,b,c,d,e], 'name2':[a,b,c,d,e],...})
3. Activate nearest-neighbors object and run the nearest neighbors algorithm, which creates tree-structures for fast and efficient searching of nearest-neighbors and spits out your top n nearest neighbors!
    In this algorithm, "representative_points" refers to the 'database' and "new_points" refers to the new user we want to match.
```
    #Initialize the NearestNeighbors model to find the 3 nearest neighbors
    n_neighbors = 3
    nearest_neighbors = NearestNeighbors(n_neighbors=n_neighbors, algorithm='auto')

    #Fit the model on the representative points
    nearest_neighbors.fit(representative_points)

    #Find the nearest neighbors for each new user
    distances, indices = nearest_neighbors.kneighbors(new_points)

    #Output the results
    for i, (dists, idxs) in enumerate(zip(distances, indices)):
        match_name_list = [representative_points_names[idx] for idx in idxs]
        user_name = new_point_names[i]
        print(f"Name:{user_name}") 
        print("Indices of Nearest Neighbors:", idxs)
        print("Names of top 3 matches:", match_name_list)
        print("Distances to Nearest Neighbors:", dists)
```
4. Report output as the name of user, list of indices of the matches, their corresponding names, and the distances between user and each match.
5. Made a dictionary for the user with the matches(key) and their corresponding distances (value).
6. The list of matched names and the dictionary of their distances are pushed into the next part of the pipeline. 
7. Visualize this matching by PCA dimension reduction and plotting the first two PCA values.
Example:
![nearest_neighbor_plot](https://github.com/user-attachments/assets/5b316d80-4301-451b-8a98-f375acdf76cd)


## Spyder Plotting Simularity Scores

#### TopMatchDict.py

The TopMatchDB Function takes the top match list outputted from [Bekah's Code] and subsets the original dictionary to just the top matches.

The EuDict Function relies on euclidean_distance and EuD4Match to build a dictionary of average euclidean distances between the user and each match, separated by attribute category.

```
def TopMatchDB(TopMatchList, DataBaseDict):
    topmatchdict = {key: DataBaseDict[key] for key in topmatchlist if key in DataBaseDict}
    return topmatchdict

#I have this dictionary. I want to calculate the distance for each sub-key
# (i.e. Agreeableness, Openness, Neuroticism, Openness, Conscientiousness)
# between the main key (i.e. SMOLLY and BIGGY and save that to a list.

# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    import math
    distance = 0.0
    for i in range(len(row1)):
        distance += (int(row1[i]) - int(row2[i])) ** 2
    return math.sqrt(distance)

# Calculate distances
def EuD4Match(Username, Matchname, data):
    distances = {}
    for trait in data[Username]:
        row1 = data[Username][trait]
        row2 = data[Matchname][trait]
        distances[trait] = euclidean_distance(row1, row2)
    return distances

#Generates Euclidean Distances for Attributes Between User and Top Matches
def EuDict(Username, filename):     #ADD TOPMATCHLIST ???
    import json 
    filename = '30UserSubbed.txt' #SUBJECT TO CHANGE
    with open(filename, 'r') as BigDB:
        data = BigDB.read()
        user_dict = json.loads(data)
    # topmatchlist = ['SMOLLY', 'Leah Huff', 'Pamela Wheeler', 'Amanda Herrera MD', 'Thomas Powell'] #READ IN???
    TopMatchDict = TopMatchDB(topmatchlist, user_dict)
     
    # Loop through topmatchlist to calculate and print Euclidean distances
    EucliDict = {}
    for topmatch in topmatchlist:
        if topmatch != Username:  # Avoid comparing SMOLLY with itself
            EuDisUserVsMatch = EuD4Match(Username, topmatch, TopMatchDict)
            #print(f"Distances between {Username} and {topmatch}: {EuDisUserVsMatch}")
            EucliDict[topmatch] = EuDisUserVsMatch
    return EucliDict

# Main execution block
if __name__ == "__main__":
    filename = '30UserSubbed.txt'
    user = 'SMOLLY'
    topmatchlist = ['SMOLLY', 'Leah Huff', 'Pamela Wheeler', 'Amanda Herrera MD', 'Thomas Powell'] #READ IN???
    EuDisUserVsMatch = EuDict(user, filename)
    print(EuDisUserVsMatch)
```
#### DictToScoreToRadar

```
def makeradar(df, user, match): #From SpyderPlot8.py
       import matplotlib.pyplot as plt
       from matplotlib.ticker import FixedLocator
       import pandas as pd
       from math import pi
       import numpy as np
       from math import sqrt
       
       categories = list(df)[1:]
       N = len(categories)
       angles = np.linspace(0, 2 * pi, N, endpoint=False)
       angles_mids = angles + (angles[1] / 2)

       fig = plt.figure(figsize=(6, 6))
       ax = plt.subplot(111, polar=True)
       ax.set_theta_offset(pi / 2)
       ax.set_theta_direction(-1)
       ax.set_xticks(angles_mids)
       ax.set_xticklabels(categories)
       ax.xaxis.set_minor_locator(FixedLocator(angles))

       # Draw ylabels
       ax.set_rlabel_position(0)
       #ax.set_yticks([20, 40, 60, 80, 100])
       #ax.set_yticklabels(["20", "40", "60", "80", "100"], color="black", size=8)
       ax.set_ylim(0, 100)
       plt.title(match, pad=20)

       values0 = df.loc[0].drop('group').values
       ax.bar(angles_mids, values0, width=angles[1] - angles[0],
              facecolor='#32CD32', alpha=0.5, edgecolor='#32CD32', linewidth=1, label="A")
       ##FF5733
       values1 = df.loc[1].drop('group').values
       ax.bar(angles_mids, values1, width=angles[1] - angles[0],
              facecolor='#FF4500', alpha=0.5, edgecolor='#FF4500', linewidth=1, label="Es")

       values2 = df.loc[2].drop('group').values
       ax.bar(angles_mids, values2, width=angles[1] - angles[0],
              facecolor='#FFFF00', alpha=0.5, edgecolor='#FFFF00', linewidth=1, label="Ex")

       values3 = df.loc[3].drop('group').values
       ax.bar(angles_mids, values3, width=angles[1] - angles[0],
              facecolor='#C8A2C8', alpha=0.5, edgecolor='#C8A2C8', linewidth=1, label="C")

       values4 = df.loc[4].drop('group').values
       ax.bar(angles_mids, values4, width=angles[1] - angles[0],
              facecolor='#87CEEB', alpha=0.5, edgecolor='#87CEEB', linewidth=1, label="O")

       ax.grid(True, axis='x', which='minor')
       ax.grid(False, axis='x', which='major')
       ax.grid(True, axis='y', which='major')
       #ax.legend(loc='upper left', bbox_to_anchor=(0.9, 1))

       try:
              user1 = user
              user2 = match
              filename = f'{user1}and{user2}.png'
              plt.savefig(filename, format='png')
              plt.close() #Not sure if needed!
              return True
       except Exception as match:
              print(f"Error Saving plot: {e}")
              return False

def SpyderScPlot(user, EuDisUserVsMatch): #We need to transform euclidean distances into a INT between 0 and 100.
        import pandas as pd
        from math import sqrt
        max_dis = sqrt(250) #This will be 5 for the pre-averaged output
        for match in EuDisUserVsMatch:
            A_dis = EuDisUserVsMatch[match]['Agreeableness']
            Es_dis = EuDisUserVsMatch[match]['Neuroticism']
            Ex_dis = EuDisUserVsMatch[match]['Extroverted']
            C_dis = EuDisUserVsMatch[match]['Conscientiousness']
            O_dis = EuDisUserVsMatch[match]['Openness']
            A_scr = int(((max_dis - A_dis)/max_dis) * 100)
            Es_scr = int(((max_dis - Es_dis)/max_dis) * 100)
            Ex_scr = int(((max_dis - Ex_dis)/max_dis) * 100)
            C_scr = int(((max_dis - C_dis)/max_dis) * 100)
            O_scr = int(((max_dis - O_dis)/max_dis) * 100)
            df = pd.DataFrame({'group': ['A', 'Es', 'Ex', 'C', 'O'], 'EXT': [0, 0, A_scr, 0, 0], 'EST': [0, Es_scr, 0, 0, 0], 'AGR': [Ex_scr, 0, 0, 0, 0], 'CSN': [0, 0, 0, C_scr, 0], 'OPN': [0, 0, 0, 0, O_scr], })
            makeradar(df, user, match) 
# Main execution block
if __name__ == "__main__":
```

Example Output:
![SpyderPlot](/Users/pfb2024/BestieBubble2/Bestie-Bubble//241027_KQScripts/SMOLLYandAmandaHerreraMD.png)

## Visual Output in the GUI
