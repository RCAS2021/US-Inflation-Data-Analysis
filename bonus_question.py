from fastapi import FastAPI
import pandas as pd

# Instanciação da aplicação
app = FastAPI()

# Definindo o Endpoint
@app.get('/inflation-data')
def read_data():
    data = pd.read_csv('inflation_data.csv')
    return data.to_dict(orient='records')

# Rodando a aplicação com uvicorn
if __name__ == 'question_1':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)