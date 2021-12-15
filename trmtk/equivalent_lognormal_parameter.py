# -*- coding: utf-8 -*-
"""
European Tsunami Risk Service
https://eurotsunamirisk.org/

This software is part of the Tsunami Risk Modeller's Toolkit

DISCLAIMER

This software is made available as a prototype implementation on behalf of
scientists and engineers for the purpose of open collaboration and in the
hope that it will be useful. It is not developed to design standards, nor
subject to critical review by professional software developers. It is
therefore distributed WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

The European Tsunami Risk Service, and the authors of the software, assume no
liability for use of the software.

"""

import numpy as np
import pandas as pd
from scipy.stats import norm


#%%
""" User input """

# Import the csv as a dataframe. Enter the name of the csv file.
data_in_csv = pd.read_csv("fragilityCurves_De_Risi_et_al_2017b_model_M3_concrete_discrete.csv")
# The vector of the intensity measure values
# Enter the name of the column containing the intensity measure.
im = np.array(data_in_csv["d_tsi (m)"])
# The vector of the probabilities
# Enter the name of the column containing the probabilities.
prob_of_ex = np.array(data_in_csv["P(DS>=DS3|d_tsi)"])


#%%
""" Computations """
# The median
eta_imc = np.interp(0.50,im,prob_of_ex)
print(eta_imc)

imc16 = np.interp(norm.cdf(-1,0,1),im,prob_of_ex)
imc84 = np.interp(norm.cdf(1,0,1),im,prob_of_ex)
beta = 0.5*np.log(imc84/imc16)
# The dispersion
print(beta)
