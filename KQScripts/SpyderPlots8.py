#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import pandas as pd
from math import pi
import numpy as np

df = pd.DataFrame({'group': ['A', 'Es', 'Ex', 'C', 'O'], 'EXT': [0, 0, 85, 0, 0], 'EST': [0, 50, 0, 0, 0], 'AGR': [25, 0, 0, 0, 0], 'CSN': [0, 0, 0, 15, 0], 'OPN': [0, 0, 0, 0, 50], })

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
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(["20", "40", "60", "80", "100"], color="black", size=8)
ax.set_ylim(0, 100)

values0 = df.loc[0].drop('group').values
ax.bar(angles_mids, values0, width=angles[1] - angles[0],
       facecolor='#FF5733', alpha=0.7, edgecolor='k', linewidth=1, label="A")

values1 = df.loc[1].drop('group').values
ax.bar(angles_mids, values1, width=angles[1] - angles[0],
       facecolor=(0.1, 0.2, 0.5, 0.3), alpha=0.7, edgecolor='k', linewidth=1, label="Es")

values2 = df.loc[2].drop('group').values
ax.bar(angles_mids, values2, width=angles[1] - angles[0],
       facecolor='#32CD32', alpha=0.7, edgecolor='#32CD32', linewidth=1, label="Es")

values3 = df.loc[3].drop('group').values
ax.bar(angles_mids, values3, width=angles[1] - angles[0],
       facecolor='y', alpha=0.7, edgecolor='y', linewidth=1, label="C")

values4 = df.loc[4].drop('group').values
ax.bar(angles_mids, values4, width=angles[1] - angles[0],
       facecolor='purple', alpha=0.7, edgecolor='purple', linewidth=1, label="O")

ax.grid(True, axis='x', which='minor')
ax.grid(False, axis='x', which='major')
ax.grid(True, axis='y', which='major')
ax.legend(loc='upper left', bbox_to_anchor=(0.9, 1))
plt.show()