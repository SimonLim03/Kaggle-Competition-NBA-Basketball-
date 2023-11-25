ADV_MLA_AT1
==============================

This is a project from assignment of Advanced Machine Learning and Algorithm.

Best models artefacts in the `models/` folder

The scripts for training and loading the team’s best models in the `src/models/` folder

Experiment reports in the `reports/` folder

The notebooks (ipynb files) stored in the `notebooks/` folder


Project Objective

The NBA draft is an annual event in which teams select players from their American colleges as well as international professional leagues to join their rosters. 

Moving to the NBA league is a big deal for any basketball player.

In this regard, the objective of the project is build a model that will predict if a college basketball player will be drafted to join the NBA league based on his statistics for the current season.

Data Source: https://www.kaggle.com/t/1f00dbe0406240ec85e3ed01b190551a

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