import pandas as pd

# Lendo o arquivo
df = pd.read_csv('inflation_data.csv')

# Filtrando dados
filtered_data = df[['CUSR0000SA0', 'CUSR0000SETB01']]

# Calculando a correlação
correlation = filtered_data['CUSR0000SA0'].corr(filtered_data['CUSR0000SETB01'])
print(f'Correlation between All items and Gasoline: {correlation}')
