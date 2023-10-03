"""
This module is an introduction to object oriented programming
in data analysis.

"""

import pandas as pd


class DataFrameAnalyzer:
    def __init__(self, data):
        self.data = data

    def summary(self):
        # calculate summary statistics
        summary = self.data.describe()
        return summary

    def filter(self, column, condition):
        # Filter data based on a condition
        filtered_data = self.data[self.data[column] == condition]
        return filtered_data


if __name__ == "__main__":
    data = pd.DataFrame({"Name": ['Alice', 'Bob', 'Charlie'],
                         "Age": [25, 30, 28]})

    analyzer = DataFrameAnalyzer(data)

    # Using methods
    summary_stats = analyzer.summary()
    filtered_data = analyzer.filter("Age", 28)

    print("Summary Statistics:")
    print(summary_stats)
    print("\nFiltered Data:")
    print(filtered_data)
