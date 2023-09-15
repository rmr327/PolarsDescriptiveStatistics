# Polars Descriptive Statistics Script Report
## Week 3 Mini Project by Rakeen Rouf

[![PythonCiCd](https://github.com/rmr327/PolarsDescriptiveStatistics/actions/workflows/python_ci_cd.yml/badge.svg)](https://github.com/rmr327/PolarsDescriptiveStatistics/actions/workflows/python_ci_cd.yml)

---

**Summary**

The objective of this week's mini project was to create a script ("polars_descriptive_statistics.py") utilizing the polars library for descriptive statistics. This script has been integrated with the Python CiCd automation template introduced in week one. A sample ouput of the script using the IRIS data set has been included at the bottom of this report. The generated report and visualization can be found in the output folder.

The main advantage of using Polars vs Pandas for data analysis is that Polars can typically handle big data better than Pandas. This is maintly becuase Polars does not need to load the entire data frame into memory at once -  therefore allowing the processing of larger data sets with limitied computing resources.

---

**Code Location**

You can find the relevant code in the following folders:
- `src`
- `test`

---

**Output Location**

Every time you run "polars_descriptive_statistics.py" from the source folder, output files will be generated at the following locations:
- `output/generated_report.md`
- `output/visualization.png`

---

**Function Descriptions**

1. `def return_25th_quantile(df: pl.DataFrame, target: str) -> float:`  
   Takes a dataframe and returns the 25th quantile of the user defined target column.

2. `def return_mean(data_: pl.DataFrame, target: str) -> float`  
   Takes in a dataframe and returns the mean of the user defined target column.

3. `def return_std_dev(data_: pl.DataFrame, target: str) -> float`  
   Takes in a dataframe and returns the standard deviation of the user defined target column.

4. `def return_median(data_: pl.DataFrame, target: str) -> float`  
   Takes in a dataframe and returns the mean of the user defined target column.

5. `def visualize_dataset(data_: pl.DataFrame, outcome_var: str, target_var: str, inteaction_term: str) -> None`  
   Visualizes the passed data. Makes a scatter plot of target vs outcome variables. Colors the scatter
   plot by the interaction term. Draws a best fit linear regression line for each category of the iinteration term. Draws vertical lines to signify the mean, median and standard deviation. Saves output visualization to a png file in the output folder. Generates a summary report in the output folder.

---

**Sample Visualization Using the IRIS data set**

Mean of sepal width = 3.06

Median of spepal width = 3.00

Standard deviation of sepal width = 0.43

![Visualization Example](https://user-images.githubusercontent.com/36940292/266804593-4fe25e4a-186c-4e49-956a-508c5d66cb05.jpg)
---
Feel free to explore the code and tests in the respective folders.
