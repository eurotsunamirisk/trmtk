# ComputeFrag
ComputeFrag is a code for computing robust fragility curves using a generalized regression model considering Hierarchical fragility modeling. This code calculates fragility curves based on maximum likelihood estimation methods (basic and hierarchical modeling) or using Bayesian model class selection (BMCS) to estimate fragility curves with their corresponding confidence bands for a set of mutually exclusive and collectively exhaustive damage states and different classes of buildings or infrastructure. The code utilizes Bayesian model class selection (BMCS) to identify the best link model to employ in the generalized linear regression scheme.

### Citation
Please consider citing the following DOI if you use ComputeFrag in your work: [DOI: 10.5281/zenodo.5167276](https://doi.org/10.5281/zenodo.5167276)

Th computefrag provides an ensemble of the fragility curves and their corresponding confidence bands for a set of mutually exclusive and collectively exhaustive (MECE) damage states (DS), where DS_i: i=0,N_DS. The fragility is defined as the probability of damage D exceeding the threshold D_i for damage state DS_i and is denoted as P(D>Di|IM). The set of damage levels (D_i, i=0,N_DS) mark the thresholds of damage states (DS_i).
The parameters of the empirical fragilities associated with different damage levels are estimated jointly using Bayesian inference by employing a Markov Chain Monte Carlo Simulation (MCMC) scheme.

![Graphical representation of damage thresholds and damage states](https://github.com/soltanisgeo/readme/blob/main/damageScale-git.png)

*Graphical representation of damage thresholds, D, and damage states, DS*


## Inputs

- **InputFileName:** The filename of a csv file containing two columns, one for the intensity measure and one for the damage state. In this example, it is the file IM_and_DS.csv.
- **NDS:** The number of damage states.
- **dIM, IM_max:** The step and the maximum absolute value for the IM vector.
- **dvec_alpha0, dvec_alpha1:** The increments of the vectors of the two logistic regression parameters.
- **confid:** The number of standard deviations defining the confidence interval for the robust fragility (fixed for all the DS).

## Outputs

- **sample_theta_model:** Ns=500 samples generated from the posterior joint probability distribution for logistic fragility model parameters (e.g., a total of 10 parameters for 5 DS, 2 parameters/DS) using the MCMC procedure.
- **rfragility:** Robust (the mean fragility among the Ns=500 realizations for each DS) fragility curve with the row showing the IM vector and a number of columns equal to the number of DS.
- **sfragility:** The standard deviation of the Ns=500 fragility curve samples (the same structure as rfragility). For having the fragility with confidence, you should do this operation: rfragility+confid*sfragility (e.g., if confid=±1, we have 16th and 84th percentiles, if confid=±2, we have 2nd and 98th percentiles).
- **etaIMc:** The median of rfragility (i.e., the IM value corresponding to 50% probability from rfragility). It is a vector with its length equal to the number of DS.
- **betaIMc:** The equivalent logarithmic standard deviation of the rfragility (i.e., half of the logarithmic distance between IM values corresponding to 84% and 16% probabilities, respectively). It is a vector with its length equal to the number of DS.

## Docker
You may also run the code as a standalone Docker application. To do so, first pull the image from [Docker Hub](https://hub.docker.com/r/eurotsunamirisk/bayesian-fragility-standalone-app). Create a folder for the input and the outputs of the code. For example, create the folder:
- `C:\input_output\` (Windows)
- `/home/user/input_output` (Linux)
Place in that folder the input file (e.g., the file `building_class_1.csv` from the code’s repository) and execute the application using one of the following commands depending on your operating system:
```sh
docker run --rm -v C:\input_output:/tmp bayesian-fragility-standalone-app /tmp/building_class_1.csv 
