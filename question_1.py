import requests
import pandas as pd
import json

def get_bls_data(series_ids, start_year, end_year):
    """
    Fetch data from the Bureau of Labor Statistics (BLS) API.

    Parameters:
    series_ids (list): List of BLS series IDs to fetch data for.
    start_year (str): The start year for the data.
    end_year (str): The end year for the data.

    Returns:
    dict: JSON response from the BLS API.
    """
    headers = {'Content-type': 'application/json'}
    data = json.dumps({
        'seriesid': series_ids,
        'startyear': start_year,
        'endyear': end_year
    })

    response = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
    return response.json()

def process_data(json_data):
    """
    Process the JSON data from the BLS API into a pandas DataFrame.

    Parameters:
    json_data (dict): JSON data from the BLS API.

    Returns:
    pd.DataFrame: Processed data in a pandas DataFrame.
    """
    data_frames = []
    for series in json_data['Results']['series']:
        series_id = series['seriesID']
        series_data = series['data']
        df = pd.DataFrame(series_data)
        df['series_id'] = series_id
        df['year_month'] = df['year'].astype(str) + '-' + df['period'].str.replace('M', '')
        df = df[['year_month', 'value', 'series_id']]
        df.columns = ['Date', 'Value', 'Series']
        data_frames.append(df)
    return pd.concat(data_frames)

series_ids = ['CUSR0000SA0', 'CUSR0000SA0L1E', 'CUSR0000SETB01']
start_year = '2019'
end_year = '2024'

# Obtain and process data
json_data = get_bls_data(series_ids, start_year, end_year)
all_data = process_data(json_data)

# Pivot data to correct format
pivot_data = all_data.pivot(index='Date', columns='Series', values='Value').reset_index()

# Save data in CSV File
pivot_data.to_csv('inflation_data.csv', index=False)

# Success Message
print("Script executed successfully! Data saved in 'inflation_data.csv'")
