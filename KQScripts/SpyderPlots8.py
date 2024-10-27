#!/usr/bin/env python3

# import matplotlib.pyplot as plt
# from matplotlib.ticker import FixedLocator
# import pandas as pd
# from math import pi
# import numpy as np
# from math import sqrt


# Categories are: (A)greeableness, (E)motional (s)tability/neuroticism, (Ex)traversion, (C)onscientiousness, and (O)penness.

#WE NEED CODE HERE THAT READS IN THE euclidean distances between
#user and person of interest for each category of questions A/Es/Ex/C/O.

# Example OUTPUT DICT (?????) = {'TopMatch1' : [Flt1, Flt2, Flt3, Flt4, Flt5], 'TopMatch2' : [Flt1, Flt2, Flt3, Flt4, Flt5], 'TopMatch3' : [Flt1, Flt2, Flt3, Flt4, Flt5]}
# TopMatches come from Neartest Neighbor Indexes
# Then we use those as Keys in a new dictionary - values list of Floats
# Floats are EuDistance for each category
# Which ???? 
JaneToEveryonDict = {'SAM' : [15.007117690507215, 1.232818367212533, 5.14426455264288, 14.295480754537278, 8.700464600184073], 'BIGGY' : [10.951623619924739, 14.432954416749684, 12.55402720518349, 12.651426201980513, 5.449679332906876], 'SMOLLY' : [7.359348076380026, 9.825220925088779, 2.3038949478616586, 12.423191453907853, 11.42640450424118]}

def DictToDis(InputDict, user, match):
       

# A_dis = 
# Es_dis = 
# Ex_dis = 
# C_dis = 
# O_dis = 



def SpyderScoresDF(A_dis, Es_dis, Ex_dis, C_dis, O_dis): #We need to transform euclidean distances into a INT between 0 and 100.
       import pandas as pd
       from math import sqrt
       max_dis = sqrt(250)
       A_scr = int((A_dis/max_dis) * 100)
       Es_scr = int((Es_dis/max_dis) * 100)
       Ex_scr = int((Ex_dis/max_dis) * 100)
       C_scr = int((C_dis/max_dis) * 100)
       O_scr = int((O_dis/max_dis) * 100)
       df = pd.DataFrame({'group': ['A', 'Es', 'Ex', 'C', 'O'], 'EXT': [0, 0, A_scr, 0, 0], 'EST': [0, Es_scr, 0, 0, 0], 'AGR': [Ex_scr, 0, 0, 0, 0], 'CSN': [0, 0, 0, C_scr, 0], 'OPN': [0, 0, 0, 0, O_scr], })
       return df 
       
#Dummy Data Scores & Data Frame
# A_scr = 85
# Es_scr = 85
# Ex_scr = 15
# C_scr = 15
# O_scr = 50
#df = pd.DataFrame({'group': ['A', 'Es', 'Ex', 'C', 'O'], 'EXT': [0, 0, A_scr, 0, 0], 'EST': [0, Es_scr, 0, 0, 0], 'AGR': [Ex_scr, 0, 0, 0, 0], 'CSN': [0, 0, 0, C_scr, 0], 'OPN': [0, 0, 0, 0, O_scr], })

def makeradar(df, user, match):
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

# Main execution block
if __name__ == "__main__":
       A_dis = 0
       Es_dis = 12
       Ex_dis = 15
       C_dis = 3
       O_dis = 8
       user = 'JANE'
       match = 'SMOLLY'
       df = SpyderScoresDF(A_dis, Es_dis, Ex_dis, C_dis, O_dis)
       makeradar(df, user, match)

