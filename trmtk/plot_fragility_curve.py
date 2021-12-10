# -*- coding: utf-8 -*-
"""
European Tsunami Risk Service
https://eurotsunamirisk.org/

This software is part of the Tsunami Risk Modeller's Toolkit

DISCLAIMER

This software is made available as a prototype implementation on behalf of
scientists and engineers for the purpose of open collaboration and in the
hope that it will be useful. It is not developed to the design standards, nor
subject to same level of critical review by professional software
developers, as GEM’s OpenQuake software suite. It is therefore distributed
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
for more details.

The European Tsunami Risk Service, and the authors of the software, assume no
liability for use of the software.

"""

import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt


#%%
""" User input """

# Import the csv as a dataframe. Enter the name of the csv file.
data_in_csv = pd.read_csv("example_fragility_curves.csv")
# The vector of the intensity measure values
# Enter the name of the column containing the intensity measure.
im = np.array(data_in_csv["d_tsi (m)"])
# The vector of the probabilities
# Enter the name of the column containing the probabilities.
prob_of_ex = np.array(data_in_csv["P(DS>=DS3|d_tsi)"])


#%%
""" Plot """

# Plot the fragility curve
fig1, ax1 = plt.subplots()
# ax.axis([0,10,0,1.0]) # define the limits of the axes
ax1.grid(True)
ax1.plot(im, prob_of_ex, linestyle='-', color=(0,0,1),
         marker='', markeredgecolor=(0,0,0), markerfacecolor=(0,0,0),
         markersize='4', label='Fragility Curve')
ax1.set_xlabel('IM')
ax1.set_ylabel('P(DS>=DS3|d_tsi)') # where h is the damage state threshold
ax1.set_title("Fragility Curve")
ax1.legend()
