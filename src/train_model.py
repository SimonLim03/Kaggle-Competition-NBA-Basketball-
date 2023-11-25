from sklearn.metrics import roc_auc_score
from sklearn.model_selection import RandomizedSearchCV

def train_classifier_model(X_train, y_train, model_class, hyperparameters=None):
    """
    Train a classifier model on the training data.

    Parameters:
        X_train (pd.DataFrame): Features for training.
        y_train (pd.Series): Labels for training.
        model_class: The class of the classifier model (e.g., RandomForestClassifier).
        hyperparameters (dict, optional): Hyperparameters for the model (default is None).

    Returns:
        trained_model: The trained classifier model.
    """
    # Create the model with optional hyperparameters
    if hyperparameters:
        model = model_class(**hyperparameters)
    else:
        model = model_class(probability= True)

    # Train the model
    model.fit(X_train, y_train)


    return model



def hyperparameter_tuning_randomized_search(model, param_dist, X, y, n_iter=10, cv=5, scoring='roc_auc'):
    """
    Perform hyperparameter tuning using RandomizedSearchCV.

    Parameters:
        model (estimator): The machine learning model to tune.
        param_dist (dict): Dictionary of hyperparameter distributions.
        X (array-like): Feature matrix.
        y (array-like): Target labels.
        n_iter (int, optional): Number of parameter settings that are sampled (default is 10).
        cv (int, cross-validation generator, or iterable, optional): Number of cross-validation folds (default is 5).
        scoring (str, callable, list, tuple, or None, optional): Scoring metric (default is 'roc_auc').

    Returns:
        RandomizedSearchCV: The fitted RandomizedSearchCV object.
    """
    random_search = RandomizedSearchCV(model, param_distributions=param_dist, n_iter=n_iter, cv=cv, scoring=scoring, n_jobs=-1)
    random_search.fit(X, y)
    
    print("Best Parameters:")
    print(random_search.best_params_)
    print(f"Best {scoring} Score: {random_search.best_score_}")
    
    return random_search