# Kaggle Competition (NBA Draft)

## Author
Name: Simon Lim

## Description
The NBA draft is an annual event in which teams select players from their American colleges as well as international professional leagues to join their rosters. 
Moving to the NBA league is a big deal for any basketball player.
In this regard, the objective of the project is build a model that will predict if a college basketball player will be drafted to join the NBA league based on his statistics for the current season.
Data Source: https://www.kaggle.com/t/1f00dbe0406240ec85e3ed01b190551a

## How to Run the Program
Execute the following steps to run the app:
- URL link: https://flight-fare-prediction-app-b5ff94ahafghdb9bxwllf5.streamlit.app/
- Fill in the input form and hit submit!
![image](https://github.com/SimonLim03/Flight-Fare-Prediction-App/assets/150989115/fd3c49b7-088a-4dba-846a-038d784f1ae5)


## Project Structure
<p>
/models: This folder contains model artefacts and CSV files of probability predictions that were used to players who can be drafted to NBA.
</p>

<p>
/notebooks: All the notebooks containing codes, preparation, EDA and precedures. 
</p>

<p>
/raw: Initial datasets.
</p>

<p>
/report: Experimental report
</p>

<p>
/src: Storage of functions used in experiments
</p>




ADV_MLA_AT1
==============================


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <- All csvs files for datasets and models   
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Notebooks for models and experiments
    │                         
    │                      
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Reports for Experiment 1, 2, 3 and Final report
    │   └── figures        
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code (functions and classes) for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
