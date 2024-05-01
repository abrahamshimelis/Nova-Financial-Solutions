# In a file called data_processing.py
import pandas as pd

# def uniform_date_format(filename, date_column, new_filename):
#     df = pd.read_csv(filename)
#     df[date_column] = pd.to_datetime(df[date_column])
#     df.to_csv(new_filename, date_format='%Y-%m-%d')

# def uniform_date_format(filename, date_column, new_filename):
#     df = pd.read_csv(filename)
#     df[date_column] = pd.to_datetime(df[date_column], format="%Y-%m-%d %H:%M:%S")
#     df.to_csv(new_filename, date_format='%Y-%m-%d')

# def uniform_date_format(filename, date_column, new_filename):
#     df = pd.read_csv(filename)
#     df[date_column] = pd.to_datetime(df[date_column], format="%Y-%m-%d %H:%M:%S%z")
#     df.to_csv(new_filename, date_format='%Y-%m-%d')

# def uniform_date_format(filename, date_column, new_filename):
#     df = pd.read_csv(filename)
#     df[date_column] = pd.to_datetime(df[date_column], infer_datetime_format=True)
#     df.to_csv(new_filename, date_format='%Y-%m-%d')

def uniform_date_format(filename, date_column, new_filename):
    df = pd.read_csv(filename)
    df[date_column] = pd.to_datetime(df[date_column], format="%Y-%m-%d %H:%M:%S%z")
    df[date_column] = df[date_column].dt.strftime('%m/%d/%Y %I:%M:%S %p %z')
    df.to_csv(new_filename)



