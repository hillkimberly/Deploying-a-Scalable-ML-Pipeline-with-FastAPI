import pytest
import numpy as np
# TODO: add necessary import

# TEST 1
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model
# TEST 2
from sklearn.metrics import precision_score, recall_score, fbeta_score
from ml.model import compute_model_metrics

# TEST 3
from sklearn.model_selection import train_test_split
from ml.data import process_data


# TODO: implement the first test. Change the function name and input as needed
# Test 1: Check if the trained model is a RandomForestClassifier (test_model_algorithim)
def test_model_algorithm():
    # add description for the first test
    """
    Verifies that the model uses the expected algorithm (RandomForestClassifier).
    """

    # Your code here

    # Mock data for training
    X_train = np.random.rand(100, 10)  # 100 samples, 10 features
    y_train = np.random.choice([0, 1], size=100)  # Binary target variable

    # Train the model
    model = train_model(X_train, y_train)

    # Check if the model is of type RandomForestClassifier
    assert isinstance(model, RandomForestClassifier), "Model is not using RandomForestClassifier"

    pass


# TODO: implement the second test. Change the function name and input as needed

# Test 2: Verify that the metrics functions return float values
def test_compute_metrics():
    """
    Verifies that the compute_model_metrics function returns float values for precision, recall, and F1 score.
    """
    # Your code here
    # Example true and predicted labels
    y_true = np.array([1, 0, 1, 1, 0, 1])
    y_pred = np.array([1, 0, 1, 0, 0, 1])

    # Compute the metrics
    precision, recall, f1 = compute_model_metrics(y_true, y_pred)

    # Assert that the returned metrics are of type float
    assert isinstance(precision, float), f"Expected float, got {type(precision)}"
    assert isinstance(recall, float), f"Expected float, got {type(recall)}"
    assert isinstance(f1, float), f"Expected float, got {type(f1)}"

    pass


# TODO: implement the third test. Change the function name and input as needed

# Test 3: Verify the training and test datasets have the expected size and type
def test_data_processing():
    """
    Verifies that the training and test datasets have the expected size and type after processing.
    """
    # Your code here
    
    # Sample dataset
    data = {
        'age': [25, 30, 35, 40],
        'workclass': ['Private', 'Self-emp', 'Private', 'Private'],
        'education': ['Bachelors', 'Masters', 'PhD', 'Bachelors'],
        'salary': ['<=50K', '>50K', '>50K', '<=50K'],
    }

    # Create a DataFrame
    import pandas as pd
    df = pd.DataFrame(data)

    # Split the data into train and test
    train, test = train_test_split(df, test_size=0.2, random_state=42)

    # Process the data using the process_data function
    X_train, y_train, encoder, lb = process_data(
        train, categorical_features=['workclass', 'education'], label='salary', training=True
    )
    X_test, y_test, _, _ = process_data(
        test, categorical_features=['workclass', 'education'], label='salary', training=False, encoder=encoder, lb=lb
    )

    # Assert that the training and test sets have the correct size and type
    assert X_train.shape[0] == 3, f"Expected 3 training samples, got {X_train.shape[0]}"
    assert X_test.shape[0] == 1, f"Expected 1 test sample, got {X_test.shape[0]}"
    assert isinstance(X_train, np.ndarray), f"Expected X_train to be a numpy array, got {type(X_train)}"
    assert isinstance(X_test, np.ndarray), f"Expected X_test to be a numpy array, got {type(X_test)}"

    pass
