import pandas as pd
import numpy as np
import unittest
from src.data_quality_check import DataQualityCheck

class TestDataQualityCheck(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5, np.nan],
            'B': [2, 3, 4, 5, 6, 100],  # 100 is an outlier
            'C': [1, 2, -3, 4, 5, 6],   # -3 is an incorrect entry
            'date_column': ['2022-12-31', '5/22/2020', '2023-01-01', '12/31/2022', '2022-01-01', '2022-06-30']
        })
        self.data_quality_check = DataQualityCheck(self.df)

    def test_check_missing_values(self):
        result = self.data_quality_check.check_missing_values()
        self.assertEqual(result['A'], 1)
        self.assertEqual(result['B'], 0)
        self.assertEqual(result['C'], 0)

    def test_check_data_type(self):
        result = self.data_quality_check.check_data_type()
        self.assertEqual(result['A'], 1)  # Numeric type (int/float)
        self.assertEqual(result['B'], 1)  # Numeric type (int/float)
        self.assertEqual(result['C'], 1)  # Numeric type (int/float)
        self.assertEqual(result['date_column'], 1)  # Object type (string)

if __name__ == '__main__':
    unittest.main()
