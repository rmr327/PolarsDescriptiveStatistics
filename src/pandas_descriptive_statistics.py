"""Python Pandas descriptive statistics script"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, Normalize
import numpy as np


def return_25th_quantile(data_: pd.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns 25th quantile of the target column"""

    target_quantile = data_[target].quantile(0.25)

    return target_quantile


def return_mean(data_: pd.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns the mean of the target column"""

    target_mean = data_[target].mean()

    return target_mean


def return_std_dev(data_: pd.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns the standard deviation of the target column"""

    target_std = data_[target].std()

    return target_std


def return_median(data_: pd.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns the mean of the target column"""

    target_median = data_[target].median()

    return target_median


def visualize_dataset(data_: pd.DataFrame, outcome_var: str, target_var: str,
                       inteaction_term: str) -> None:
    """Visualizes the passed data. Makes a scatter plot of target vs outcome
    variables. Colors the scatter plot by the interaction term. Draws a best
    fit linear regression line for each category of the iinteration
    term. Draws vertical lines to signify the mean, median and standard
    deviation."""

    # Get the unique categories from the interaction_term column
    categories = data_[inteaction_term].unique()
    # Define a colormap based on the number of unique categories
    cmap = plt.cm.get_cmap("tab10", lut=len(categories))

    # Create a ListedColormap with normalized values
    norm = Normalize(vmin=0, vmax=len(categories) - 1)
    colors = [cmap(norm(i)) for i in range(len(categories))]
    custom_cmap = ListedColormap(colors)

    # Add scatter plot of outcome vs predictor
    plt.scatter(
        data_[target_var],
        data_[outcome_var],
        c=data_[inteaction_term].apply(lambda x: list(categories).index(x)),
        cmap=custom_cmap)

    # Add labels
    plt.xlabel(target_var)
    plt.ylabel(outcome_var)
    plt.title(f"Descriptive Statistics {target_var} VS {outcome_var}")

    # Fitting and plotting linear regression models for each interaction term category
    for cat in categories:
        data_c = data_.loc[data_[inteaction_term] == cat]

        slope, intercept = np.polyfit(data_c[target_var], data_c[outcome_var], 1)
        best_fit_line = slope * data_c[target_var] + intercept

        plt.plot(data_c[target_var],
                best_fit_line,
                label=f'Best Fit For Interaction Category: {cat}')


    # Plot mean, median, std dev, and 25th quantil;e
    mean = return_mean(data_, target_var)
    plt.axvline(x=mean, color='red', linestyle='--', label=f'Mean: {mean:.2f}')

    median = return_median(data_, target_var)
    plt.axvline(x=median, color='green', linestyle='--', label=f'Median: {median:.2f}')

    stand_dev = return_std_dev(data_, target_var)
    plt.axvline(x=mean + stand_dev, color='orange', linestyle='--',
                label=f'Mean + StDev: {stand_dev + mean:.2f}')
    plt.axvline(x=mean - stand_dev, color='orange', linestyle='--',
                label=f'Mean - StDev: {mean - stand_dev:.2f}')

    plt.legend()
    plt.show()
    visualization_path = 'output/visualization.png'
    plt.savefig(visualization_path)  # save png

    # Save generated report
    summary_report_path = r'output/generated_report.md'
    with open(summary_report_path, "w", encoding="utf-8") as report:
        report.write(f'Mean: {round(mean, 3)} \n \n \n')
        report.write(f'Median: {round(median, 3)} \n \n \n')
        report.write(f'Standard Deviation: {round(stand_dev, 3)} \n \n \n')
        report.write("\n![Visualization](visualization.png)\n")


if __name__ == "__main__":
    data = pd.read_csv("data/iris_data.csv")
    TARGET_COLUMN = "sepal_width"

    print(return_25th_quantile(data, TARGET_COLUMN))
    print(return_mean(data, TARGET_COLUMN))
    print(return_median(data, TARGET_COLUMN))
    print(return_std_dev(data, TARGET_COLUMN))

    visualize_dataset(data, "petal_width", TARGET_COLUMN, "species")
