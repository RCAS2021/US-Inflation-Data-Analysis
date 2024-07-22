import pandas as pd

# Reading csv file
df = pd.read_csv('inflation_data.csv')

# Filtering data
filtered_data = df[['CUSR0000SA0', 'CUSR0000SETB01']]

# Calculating correlation
correlation = filtered_data['CUSR0000SA0'].corr(filtered_data['CUSR0000SETB01'])
print(f'Correlation between All items and Gasoline: {correlation}')
