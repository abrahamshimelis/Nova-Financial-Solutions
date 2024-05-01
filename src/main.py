import pandas as pd
from scipy import stats
import numpy as np
from data_quality_check import DataQualityCheck  # Assuming data_quality_check.py contains the DataQualityCheck class
from uniform_date_format import uniform_date_format

# Read the CSV file into a pandas DataFrame
file_path = 'data/raw_analyst_ratings.csv'
df = pd.read_csv(file_path)

# Instantiate the DataQualityCheck class with the DataFrame
data_checker = DataQualityCheck(df)

# Perform data quality checks
missing_values_summary = data_checker.check_missing_values()
print("Missing Values Summary:")
print(missing_values_summary)

# Call the check_data_type method to get the data type counts
data_type_counts = data_checker.check_data_type()

# Call the check_data_type method to get the data type counts
data_type_counts = data_checker.check_data_type()

# Print the data type counts 
print("Data Type Counts:")
for column, count in data_type_counts.items():
    print(f"{column}: {count}")

# Make the date column uniform date format
uniform_date_format(file_path, 'date', 'data/uniform_analyst_ratings.csv')


