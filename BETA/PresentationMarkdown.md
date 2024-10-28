# PFB 2024 Project: Bestie Bubble

**Isobel Fetter, Harshad Ingle, Bekah Kim, Konstantin Queitsch, Lola Takhirov | Riley Kellermeyer**

## Project Goals:
* Build a GUI to uptake new user information and inputs. 
* Read in 1) numerical survey 2) categorical survey data for users into complex data structures in Python.
* Leverage K-Nearest Neighbors Algorithm to determine top matches based on similarity and plot clusters.
* Calculate Simularity Scores using Euclidean Distances and plot simuleratiy.
* Extend GUI for visual disply of plotted outputs for BestieBubbles&trade;.

## Building the GUI 
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
## K-Nearest Neighbors Algorithm on Numerical Data
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