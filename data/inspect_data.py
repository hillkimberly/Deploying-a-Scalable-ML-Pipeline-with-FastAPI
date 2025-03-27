import pandas as pd

# Load the census data from the file path
file_path = 'data/census.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data
print(data.head())
