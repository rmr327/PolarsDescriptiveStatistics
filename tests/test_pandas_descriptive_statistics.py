"""Test script for pandas descriptive statistics script"""
import sys
from math import floor
import pandas as pd
import matplotlib.pyplot as plt
sys.path.append("/workspaces/PandasDescriptiveStatisitcs")
from src.pandas_descriptive_statistics import return_25th_quantile, return_mean
from src.pandas_descriptive_statistics import return_std_dev, return_median, visualize_dataset


def test_return_25th_quantile():
    """Test function for return_25th_quantile"""
    data = pd.read_csv("data/iris_data.csv")
    target_column = 'sepal_width'

    res =  return_25th_quantile(data, target_column)

    # hand calculations
    data = data.sort_values(by=target_column)
    quan_25th = data.iloc[floor(data.shape[0] / 4)][target_column]

    assert res == quan_25th


def test_return_mean():
    """Test function for return_mean"""
    data = pd.read_csv("data/iris_data.csv")
    target_column = 'sepal_width'

    # hand calculation
    expected_mean_a = sum(data[target_column]) / len(data[target_column])

    # function calculation
    calculated_mean_a = return_mean(data, target_column)

    # Check if the calculated mean matches the expected mean
    assert round(calculated_mean_a) == round(expected_mean_a)


def test_return_std_dev():
    """Test function for return_std_dev"""
    data = {'A': [1, 2, 3, 4, 5]}
    data = pd.DataFrame(data)

    result = return_std_dev(data, 'A')

    assert isinstance(result, float)
    assert round(result, 2) == 1.58

def test_return_median():
    """Test function for return_median"""
    data = pd.read_csv("data/iris_data.csv")
    target_column = 'sepal_width'

    # hand calculation
    expected_median = data[target_column].median()

    # function calculation
    calculated_median = return_median(data, target_column)

    # Check if the calculated mean matches the expected mean
    assert round(calculated_median) == round(expected_median)

def test_visualize_dataset():
    """Testing function for visualization"""

    data = pd.read_csv("data/iris_data.csv")
    target_column = 'sepal_width'
    outcome_column = 'petal_width'
    interaction_col = 'species'

    # Test if the function executes without errors
    visualize_dataset(data, outcome_column, target_column, interaction_col)

    # Capture the plot output and check if it's not empty
    fig = plt.gcf()
    assert len(fig.axes) > 0


if __name__ == '__main__':
    test_visualize_dataset()
    test_return_std_dev()
    test_return_25th_quantile()
    test_return_mean()
    test_return_median
