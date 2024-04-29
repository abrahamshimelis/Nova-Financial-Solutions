from scipy import stats
import numpy as np
from dateutil import parser
from collections import defaultdict

class DataQualityCheck:
    def __init__(self, df):
        self.df = df
    # checking for empty values
    def check_missing_values(self):
        return self.df.isnull().sum()

    # checking for different data types
    def check_data_type(self):
        data_type_counts = {}
        for column in self.df.columns:
            data_type_counts[column] = self.df[column].apply(lambda x: type(x)).nunique()
        return data_type_counts