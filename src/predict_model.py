def predict_probabilities_test(model, X_test):
    """
    Predict prediction probabilities for a test dataset.

    Parameters:
    - model
    - X_test

    Returns:
    - prob_predictions: Predicted class probabilities.
    """
    # Predict class probabilities
    prob_predictions = model.predict_proba(X_test)

    # Return the predicted probabilities
    return prob_predictions

def predict_probabilities_train(model, X_train):
    """
    Predict prediction probabilities for a train dataset.

    Parameters:
    - model
    - X_train

    Returns:
    - prob_predictions: Predicted class probabilities.
    """
    # Predict class probabilities
    prob_predictions = model.predict_proba(X_train)

    # Return the predicted probabilities
    return prob_predictions