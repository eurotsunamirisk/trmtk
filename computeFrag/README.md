# ComputeFrag

ComputeFrag is a code for computing robust fragility curves using a generalized regression model considering Hierarchical fragility modeling. This code calculates fragility curves based on maximum likelihood estimation methods (basic and hierarchical modeling) or using Bayesian model class selection (BMCS) to estimate fragility curves with their corresponding confidence bands for a set of mutually exclusive and collectively exhaustive damage states and different classes of buildings or infrastructure. The code utilizes Bayesian model class selection (BMCS) to identify the best link model to employ in the generalized linear regression scheme.

**Citation:** Please consider citing the following DOI if you use ComputeFrag in your work: [DOI: 10.5281/zenodo.5167276](https://doi.org/10.5281/zenodo.5167276)

![Graphical representation of damage thresholds and damage states](https://github.com/soltanisgeo/readme/blob/main/damageScale-git.png)

*Graphical representation of damage thresholds, D, and damage states, DS*

## Inputs

- **Filename:** The filename of a CSV file containing two columns, one for the intensity measure and one for the damage state.
- **output_folder:** The folder where the outputs will be stored.
- **excel_filename:** The name of the Excel file for storing the fragility data.
- **D:** Definition of the damage levels (e.g., 0:2 showing that we have 3 damage levels 0, 1, and 2).
- **dvec_alpha0, dvec_alpha1:** The increments of the vectors of the two logistic regression parameters.
- **do_MCMC_M1, do_MCMC_M2, do_MCMC_M3:** Perform MCMC for fragility models 1, 2, and 3 (if 0, do not perform MCMC; if 1, perform MCMC).
- **COVprior_M1, COVprior_M2, COVprior_M3:** Coefficient of variation for the prior parameters of models 1, 2, and 3.
- **dIM, IM_max:** The step and the maximum absolute value for the IM vector.
- **confidence:** The number of standard deviations defining the confidence interval for the robust fragility (fixed for all the DS).
- **do_modelClassSelection:** If 0, do not perform model class selection; if 1, do model class selection.

## Outputs

- **sample_theta_model:** Ns=500 samples generated from the posterior joint probability distribution for logistic fragility model parameters.
- **rfragility:** Robust fragility curve (the mean fragility among the Ns=500 realizations for each DS).
- **sfragility:** The standard deviation of the Ns=500 fragility curve samples.
- **etaIMc:** The median of rfragility.
- **betaIMc:** The equivalent logarithmic standard deviation of the rfragility.

## Docker

You may also run the code as a standalone Docker application. To do so, first pull the image from [Docker Hub](https://hub.docker.com/r/eurotsunamirisk/bayesian-fragility-standalone-app). Create a folder for the input and the outputs of the code, place the input file (e.g., `building_class_1.csv`), and execute the application using one of the following commands depending on your operating system:

```sh
docker run --rm -v C:\input_output:/tmp bayesian-fragility-standalone-app /tmp/building_class_1.csv 
