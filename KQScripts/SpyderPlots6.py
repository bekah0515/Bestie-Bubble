#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def pie_radar_chart(data, labels):
    N = len(data)
    theta = np.linspace(0, 2 * np.pi, N, endpoint=False)

    # Create a figure and polar axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')

    # Plot the radar chart
    ax.plot(theta, data, color='k')
    ax.fill(theta, data, alpha=0.25)

    # Add labels
    ax.set_xticks(theta)
    ax.set_xticklabels(labels)

    # Set the y-axis limits
    ax.set_ylim(0, max(data) * 1.1)

    plt.show()

# Example data
data = [30, 25, 40, 15, 20]
labels = ['A', 'B', 'C', 'D', 'E']

# Create the chart
pie_radar_chart(data, labels)