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
GNU General Public License for more details:
https://www.gnu.org/licenses/gpl-3.0.html

The European Tsunami Risk Service, and the authors of the software, assume no
liability for use of the software.

"""

import numpy as np



def glm_probit_lognormal(im, prob_of_ex):
    """
    This function takes as input a set of points defined by values of an
    intensity measure and the corresponding probabilities, and computes the
    mean and the dispersion of a lognormal curve. More information on this
    procedure may be found here: https://doi.org/10.1007/s00024-019-02245-w
    
    Usage:
    median, dispersion = glm_probit_lognormal( \
                             im=im_1d_vector, prob_of_ex=prob_1d_vector)
        
    median: the median of the lognormal CDF
    dispersion: the dispersion of the lognormal CDF
    
    im: the values of the intensity measure
    prob_of_ex: the values of the probability at the intensity measure
                values in "im". "prob_of_ex" must have the same length as
                "im"
                
    Note: unless there are at least 2 points with a probabilities > 0 AND
          < 1, the function will return NaNs
    """
    from scipy.stats import norm
    
    # Censor the data for probabilities equal to 0 and 1, because the probit
    # link function returns infinite values in these cases
    
    im = np.delete(im,prob_of_ex==0)
    prob_of_ex = np.delete(prob_of_ex,prob_of_ex==0)
    im = np.delete(im,prob_of_ex==1)
    prob_of_ex = np.delete(prob_of_ex,prob_of_ex==1)
    
    # Computation of the parameters of the fragility curve
    # If there are less than 2 point probabilities, the function returns NANs
    if len(prob_of_ex)>=2:
        # The probit link function
        Y = norm.ppf(prob_of_ex)
        # Ordinary least squares regression
        A = np.array([np.ones(len(im)), np.log(im)])
        # C is the vector of the parameters of the generalized linear model
        C = np.linalg.inv( A @ np.transpose(A) ) @ A @ Y
        # If C[1] is not positive the function retures NANs
        if C[1]>0:
            # The median and the dispersion of the fragility curve
            median = np.exp(-C[0]/C[1])
            dispersion = 1 / C[1]
        else:
            median = np.NAN
            dispersion = np.NAN
    
    return median, dispersion



def glm_logit_logistic(im, prob_of_ex):
    """
    This function takes as input a set of points defined by values of an
    intensity measure and the corresponding probabilities, and computes the
    parameters of a logistic curve.
    
    Usage:
    beta_0, beta_1 = glm_logit_logistic( \
                         im=im_1d_vector, prob_of_ex=prob_1d_vector)
        
    beta_0, beta_1: the parameters of the logistic curve. To cumpute the
    logistic curve use the following command:
        scipy.special.expit( beta_0 + beta_1 * x )
    
    im: the values of the intensity measure
    prob_of_ex: the values of the probability at the intensity measure
                values in "im". "prob_of_ex" must have the same length as
                "im"
              
    Note: unless there are at least 2 points with a probabilities > 0 AND
          < 1, the function will return NaNs
    """
    from scipy.special import logit
    
    # Censor the data for probabilities equal to 0 and 1, because the logit
    # link function returns infinite values in these cases
    
    im = np.delete(im,prob_of_ex==0)
    prob_of_ex = np.delete(prob_of_ex,prob_of_ex==0)
    im = np.delete(im,prob_of_ex==1)
    prob_of_ex = np.delete(prob_of_ex,prob_of_ex==1)
    
    # Computation of the parameters of the fragility curve
    # If there are less than 2 point probabilities, the function returns NANs
    if len(prob_of_ex)>=2:
        # The logit link function
        Y = logit(prob_of_ex)
        # Ordinary least squares regression
        A = np.array([np.ones(len(im)), im])
        # C is the vector of the parameters of the generalized linear model
        C = np.linalg.inv( A @ np.transpose(A) ) @ A @ Y
        # If C[1] is not positive the function retures NANs
        if C[1]>0:
            # The parameters of the logistic curve
            beta_0 = C[0]
            beta_1 = C[1]
        else:
            beta_0 = np.NAN
            beta_1 = np.NAN
    
    return beta_0, beta_1