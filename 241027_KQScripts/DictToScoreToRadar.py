#!/usr/bin/env python3
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import pandas as pd
from math import pi
import numpy as np
from math import sqrt


# Categories are: (A)greeableness, (E)motional (s)tability/neuroticism, (Ex)traversion, (C)onscientiousness, and (O)penness.

# def EuDict2EuScore(user, EuDisUserVsMatch): NAH! EASIER TO DO IN ONE FUNCTION.
#     for match in EuDisUserVsMatch:
#         A_dis = EuDisUserVsMatch[match]['Agreeableness']
#         Es_dis = EuDisUserVsMatch[match]['Neuroticism']
#         Ex_dis = EuDisUserVsMatch[match]['Extroverted']
#         C_dis = EuDisUserVsMatch[match]['Conscientiousness']
#         O_dis = EuDisUserVsMatch[match]['Openness']
#         return A_dis, Es_dis, Ex_dis, C_dis, O_dis

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
    EuDisUserVsMatch = {'Leah Huff': {'Agreeableness': 5.830951894845301, 'Extroverted': 5.0, 'Openness': 5.0, 'Conscientiousness': 5.916079783099616, 'Neuroticism': 6.0},
 'Pamela Wheeler': {'Agreeableness': 4.358898943540674, 'Extroverted': 4.47213595499958, 'Openness': 7.54983443527075, 'Conscientiousness': 5.385164807134504, 'Neuroticism': 4.69041575982343},
  'Amanda Herrera MD': {'Agreeableness': 4.47213595499958, 'Extroverted': 7.3484692283495345, 'Openness': 2.6457513110645907, 'Conscientiousness': 4.123105625617661, 'Neuroticism': 4.795831523312719},
   'Thomas Powell': {'Agreeableness': 3.7416573867739413, 'Extroverted': 4.123105625617661, 'Openness': 2.8284271247461903, 'Conscientiousness': 6.6332495807108, 'Neuroticism': 5.916079783099616}}
    user = 'SMOLLY'
    SpyderScPlot(user, EuDisUserVsMatch)
    

    





