import plotly.express as px
import pandas as pd

# Lendo arquivo
data = pd.read_csv('inflation_data.csv')

# Filtrando dados
filtered_data = data[['Date', 'CUSR0000SA0L1E']].copy()

# Corrigindo tipo da coluna data
filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])

# Calculando porcentagem de mudança anual
filtered_data = filtered_data.set_index('Date').resample('MS').mean()
filtered_data['YoY Change'] = filtered_data['CUSR0000SA0L1E'].pct_change(12) * 100

# Criando gráfico
fig = px.line(filtered_data, x=filtered_data.index, y='YoY Change', title='Year-over-Year Change for All items, less food and energy')
fig.update_xaxes(dtick="M1", tickformat="%b\n%Y")
fig.show()
