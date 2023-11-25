import pandas as pd
import numpy as np

def drop_columns(data):
    """
    Drop specified columns from a DataFrame.

    Parameters:
        data (pd.DataFrame): The DataFrame from which columns need to be dropped.

    Returns:
        pd.DataFrame: The DataFrame with specified columns dropped.
    """
    columns_to_drop = ['pick', 'Rec_Rank', 'dunks_ratio']
    data = data.drop(columns=columns_to_drop, inplace=True)
    return data


def fill_missing_with_mean(data, columns_to_fill):
    """
    Fill missing values in specified columns with their mean values.

    Parameters:
        data (pd.DataFrame): The DataFrame in which missing values need to be filled.
        columns_to_fill (list): List of column names to fill missing values.

    Returns:
        pd.DataFrame: The DataFrame with missing values filled with mean values.
    """
    for column in columns_to_fill:
        data[column].fillna(data[column].mean(), inplace=True)
    return data

def separate_numeric_categorical_columns(train_data, test_data):
    """
    Separate numeric and categorical columns in the training and testing DataFrames.

    Parameters:
        train_data (pd.DataFrame): The training DataFrame.
        test_data (pd.DataFrame): The testing DataFrame.

    Returns:
        num_cols_train (pd.DataFrame): Numeric columns in the training DataFrame.
        cat_cols_train (pd.DataFrame): Categorical columns in the training DataFrame.
        num_cols_test (pd.DataFrame): Numeric columns in the testing DataFrame.
        cat_cols_test (pd.DataFrame): Categorical columns in the testing DataFrame.
    """
    num_cols_train = train_data.select_dtypes(exclude='object')
    cat_cols_train = train_data.select_dtypes(include='object')
    num_cols_test = test_data.select_dtypes(exclude='object')
    cat_cols_test = test_data.select_dtypes(include='object')

    return num_cols_train, cat_cols_train, num_cols_test, cat_cols_test

def replace_values_in_columns(training_data, testing_data):
    """
    Replace specific values in 'num' and 'yr' columns of training and testing DataFrames.

    Parameters:
        training_data (pd.DataFrame): The training DataFrame.
        testing_data (pd.DataFrame): The testing DataFrame.

    Returns:
        training_data (pd.DataFrame): Training DataFrame with values replaced.
        testing_data (pd.DataFrame): Testing DataFrame with values replaced.
    """
    # Replacements for 'num' column
    num_replacements = {
        'None': 0,
        '23B': '23',
        '4A': '4',
        '31/24': '31',
        '--': '0'
    }

    training_data['num'].replace(num_replacements, inplace=True)
    testing_data['num'].replace(num_replacements, inplace=True)


    # Replacements for 'yr' column
    yr_replacements = {
        'Fr': 1,
        'So': 2,
        'Jr': 3,
        'Sr': 4,
        'None': 0
    }

    training_data['yr'].replace(yr_replacements, inplace=True)
    testing_data['yr'].replace(yr_replacements, inplace=True)


    return training_data, testing_data

def convert_columns_to_num(training_data, testing_data):
    """
    Convert 'num' column to float and 'yr' column to int in training and testing DataFrames.

    Parameters:
        training_data (pd.DataFrame): The training DataFrame.
        testing_data (pd.DataFrame): The testing DataFrame.

    Returns:
        training_data (pd.DataFrame): Training DataFrame with columns converted.
        testing_data (pd.DataFrame): Testing DataFrame with columns converted.
    """
    training_data['num'] = training_data['num'].astype(float)
    testing_data['num'] = testing_data['num'].astype(float)

    training_data['yr'] = training_data['yr'].astype(int)
    testing_data['yr'] = testing_data['yr'].astype(int)

    return training_data, testing_data