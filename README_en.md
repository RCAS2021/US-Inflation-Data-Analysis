# US Inflation Data Analysis
## Automation challenge for data collection, transformation, and visualization of U.S. inflation data, and API creation for data requests.

## Challenges:

### Question 1 (question_1.py): 
- Obtain the following U.S. inflation series (CPI) via the Bureau of Labor Statistics API:
    - CPI All items, seasonally adjusted
    - CPI All items, less food and energy, seasonally adjusted
    - CPI Gasoline (all types), seasonally adjusted

- Process the data and format the columns to the format (date/series1/series2/series3)
- Save the results in a CSV file

#### Steps:

- Go to the website: https://www.bls.gov/
- Find the series in the data tools under Inflation & Prices - All Urban Consumers (Current Series)
- In the One Screen tool, select the requested items: CPI - All Items, CPI - All Items less food and energy, and CPI - Gasoline (All types), all seasonally adjusted.
- The series found are: 
    - U.S. city average All items Seasonally Adjusted: CUSR0000SA0
    - U.S. city average All items less food and energy Seasonally Adjusted: CUSR0000SA0L1E
    - U.S. city average Gasoline (all types) Seasonally Adjusted: CUSR0000SETB01

- With the series identified, fetch the data via API (main.py with the function get_bls_data()) and then process the data (main.py with the function process_data())
- Save the processed data to a CSV file

### Question 2 (question_2.py):
Using Plotly, develop a chart displaying the year-over-year percentage variation of the series All items, less food and energy, seasonally adjusted, using monthly data from 2019 to the present, maintaining a monthly frequency.

#### Steps:
- Read the inflation_data.csv file
- Filter the dataframe for the CUSR0000SA0L1E series
- Add the year-over-year percentage change
- Generate the chart

### Question 3:
Describe how to automate the data extraction process.

#### Steps:
To automate the data extraction process, I would schedule the execution of the question_1.py script using Task Scheduler (Windows) or Cron (Linux).

**Linux Cron:**
- Add execution permission to the script: `chmod +x /path/to/script/question_1.py`
- Add an entry to crontab for monthly execution:
    ```bash
    0 0 1 * * /usr/bin/python3 /path/to/script/question_1.py >> /path/to/log/inflation_data.log 2>&1
    ```
- Save and exit
- Verify if it was created correctly: `crontab -l`

**Windows Task Scheduler:**
- Create a basic task
- Add a monthly trigger and set the date and time for the script execution
- In "Start a Program", in the "Program/script" field, enter the path to the Python interpreter
- In "Add arguments", enter the path to the question_1.py script
- Finish the setup
- Verify the execution

### Question 4 (question_4.py):
Explain how to relate the All items and Gasoline series

#### Steps:
Calculating the correlation between the two series:
- Reading the inflation_data.csv file
- Filtering the data for the two columns
- Calculating the correlation using the corr() function

### Bonus Question (bonus_question.py):
Create an API with FastAPI for requests of the data stored in the CSV file.

#### Steps:
- Create the API with an HTTP GET endpoint for the requests
- Create a web server using uvicorn