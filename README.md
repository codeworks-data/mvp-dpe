# Use Case #2: Predicting Buildings' Energy Consumption using Machine Learning

## Project Scope:

In this project, we look at DPE (Diagnostic de Performance Énergétique) data from France, analyse it and build ML models that predict the energy consumption of a building as well as its greenhouse gas emissions.

The correnponsing medium article:  

## Table of contents
* [Data source](#data-source)
* [Technologies](#technologies)
* [Files](#Files)

## Data source
We use a public French government dataset.
https://data.ademe.fr/datasets/dpe-france

Each row details a building diagnosis with data ranging from the diagnosis date, the building description to the two labels assigned to each building.
The diagnoses span from 2001 to 2020 (as of today).

## Technologies
|  Technologies | Version  |
|---|---|
|  pandas | 1.1.5 |
|  numpy | 1.20.0 | 
|  plotly| 4.14.3 |
|  matplotlib |  3.2.2  |
|  seaborn |  0.11.1  |
|  datapane |  0.10.5 |

## Files
### Notebooks
- Sample_DPE_Data.ipynb: this notebook contains the code for sampling 5% of the data to use in modeling.
- EDA.ipynb: This notebook details the exploratory data analysis 

### Data
- data_sample.zip: contains the 5% sample extracted from the original data set. Contains about 500k rows.

