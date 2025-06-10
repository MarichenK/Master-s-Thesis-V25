# Master-s-Thesis-V25
This repository contains all the code used to generate plots and figures for my Master's Thesis in Biophysics 2025. The article is not public.

## StatisticalAnalysis.ipynb
Code for checking the normality distribution, where the Shapiro-Wilk test is run. Shapiro-Wilk fits well with cohort samples n < 50. 
Code for running comparisons between the cohorts. If normality is detected, a paired t-test is run. Otherwise, a Wilcoxon signed-rank test will be run. 
Code for running Cohen's d effect size. This is included as a supplementary test because of the small sample size.
An additional independent normality distribution test is also included. This test has been used to determine which measure best describes the data (Median vs. Mean). 

## ADCFeatureAnalysis.ipynb
This code takes in a feature .nii file from Proviz. Everything with voxel intensity = 0 is disregarded as not a part of the ROI. 
All slices are iterated through. A mean ADC is found for each slice, and then a mean of the mean is determined. 
Minimum and maximum values for each slice and the location of the minimum voxel value are also found. 
Code for plotting the box plot representation of the results is also included in this Notebook.

## CorrelationAnalysis.ipynb
Code that calculates the correlation between metrics through a linear regression. Pearson's r and Spearman's rho are calculated to explain trends in the scatter plots better. 
Code to plot the results is also included. Seaborn regplots (scatter), individual for DSC and HD95. 
An additional script for making the same analysis with filtered data (without outliers) is also included in the Notebook.

## 3DSlicerScript.py
This Python script can be used in the Python console in 3D Slicer. 
It sets all values more than 0 to 1, making it binary.

## DSCcalc.py
Code that calculates the DSC between two ROIs. Case name, MR sequence, and ROIs needs to be specified. 

## HD95calc.py
Code that calculates the HD95 between two ROIs. Case name, MR sequence, and ROIS needs to be specified.
Distance is given in cm. 


