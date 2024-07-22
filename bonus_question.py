from fastapi import FastAPI
import pandas as pd

# Instantiating app
app = FastAPI()

# Defining endpoint
@app.get('/inflation-data')
def read_data():
    data = pd.read_csv('inflation_data.csv')
    return data.to_dict(orient='records')

# Running app with uvicorn web server
if __name__ == 'question_1':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
