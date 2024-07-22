import plotly.express as px
import pandas as pd

# Reading csv file
data = pd.read_csv('inflation_data.csv')

# Filter data
filtered_data = data[['Date', 'CUSR0000SA0L1E']].copy()

# Correcting date column data type
filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])

# Calculating year to year change percentage
filtered_data = filtered_data.set_index('Date').resample('MS').mean()
filtered_data['YoY Change'] = filtered_data['CUSR0000SA0L1E'].pct_change(12) * 100

# Creating chart
fig = px.line(filtered_data, x=filtered_data.index, y='YoY Change', title='Year-over-Year Change for All items, less food and energy')
fig.update_xaxes(dtick="M1", tickformat="%b\n%Y")
fig.show()
