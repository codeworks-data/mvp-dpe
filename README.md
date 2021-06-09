# Use Case #2: Predicting Buildings' Energy Consumption using Machine Learning

## Project Scope

In this project, we look at DPE (Diagnostic de Performance Énergétique) data from France, analyse it and build ML models that predict the energy consumption of a building as well as its greenhouse gas emissions.

The correnponsing medium article:
Part 1: https://medium.com/codeworksparis/use-case-2-predicting-buildings-energy-consumption-using-machine-learning-589f1ffc34ea
Part 2 : https://medium.com/codeworksparis/use-case-2-predicting-buildings-energy-consumption-using-machine-learning-dd771f9ae122

## Table of contents
* [Data source](#data-source)
* [Technologies](#technologies)
* [Files](#Files)
* [MLflow](#MLflow)
* [Plots](#Plots)

## Data source
We use a public French government dataset.
https://data.ademe.fr/datasets/dpe-france

Each row details a building diagnosis with data ranging from the diagnosis date, the building description to the two labels assigned to each building.
The diagnoses span from 2001 to 2020 (as of today).

## Technologies
|  Technologies | Version  |
|---|---|
|  catboost| 0.26 |
|  category-encoders | 2.2.2 |
|  datapane |  0.10.5 |
|  lightgmb | 2.2.3 |
|  matplotlib |  3.2.2  |
|  mlflow | 1.17.0 |
|  numpy | 1.20.0 | 
|  pandas | 1.1.5 |
|  plotly| 4.14.3 |
|  scikit-learn | 0.22.2.post1 |
|  seaborn |  0.11.1  |
|  shap | 0.39.0 |

## Files
### Notebooks
- **Sample_DPE_Data.ipynb**: This notebook contains the code for sampling 5% of the data to use in modeling.
- **EDA.ipynb**: This notebook details the exploratory data analysis.
- **temperatures.ipynb**: This notebook contains the analysis and grouping of temperature data.
- **models.ipynb**: This notebook details the modelling pipeline.

### Data
- data_sample.zip: contains the 5% sample extracted from the original data set. Contains about 500k rows.
- temperature-quotidienne-departementale.csv: raw temperature data.
- temperatures.csv: clean temperature dataset.

### MLflow
- Mlflow tracking experiments.

### Plots
- Performance plots.

