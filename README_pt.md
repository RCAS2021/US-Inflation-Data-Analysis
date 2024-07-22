# US Inflation Data Analysis
## Desafio de automação de coleta, transformação e visualização de dados sobre a inflação nos Estados Unidos e criação de API para obter requisições dos dados.

## Desafios:

### Questão 1 (question_1.py): 
- Obter as seguintes séries de inflação dos Estados Unidos (CPI) via API da Secretaria de Estatísticas Trabalhistas:
    - CPI All items, seasonally adjusted
    - CPI All items, less food and energy, seasonally adjusted
    - CPI Gasoline (all types), seasonally adjusted

- Processar os dados e formatar as colunas para o formato (data/serie1/serie2/serie3)
- Salvar os resultados em arquivo CSV

#### Passos:

- Entrar no site: https://www.bls.gov/
- Encontrar as séries no Data Tools em Inflation & Prices - All Urban Consumers (Current Series)
- No One Screen, selecionar os itens requisitados, ou seja, CPI - All Items, CPI - All Items less food and energy e CPI - Gasoline (All types), todos com ajuste sazonal.
- As séries encontradas foram: 
    - U.S. city average All items Seasonally Adjusted: CUSR0000SA0
    - U.S. city average All items less food and energy Seasonally Adjusted: CUSR0000SA0L1E
    - U.S. city average Gasoline (all types) Seasonally Adjusted: CUSR0000SETB01

- Tendo as séries, agora pegar os dados via API (main.py com a função get_bls_data()) e então processar os dados (main.py com a função process_data())
- Com os dados processados, salvar esses dados em arquivo CSV

### Questão 2 (question_2.py):
Usando Plotly, desenvolver um gráfico exibindo o percentual de variação ano a ano da série All items, less food and energy com ajuste sazonal, usando os dados mensais de 2019 até o presente, com frequência mensal.

#### Passos:
- Ler o arquivo inflation_data.csv
- Filtrar o dataframe com a série CUSR0000SA0L1E
- Adicionar a porcentagem de mudança anual
- Gerar o gráfico

### Questão 3:
Descrever como automatizar o processo de extração de dados.

#### Passos:
Para automatizar o processo de extração dos dados, eu criaria um agendamento para a execução do script question_1.py através do Task Scheduler (Windows) ou Cron (Linux).

**Linux Cron:**
- Adicionar permissão ao script: `chmod +x /caminho/script/question_1.py`
- Adicionar entrada no crontab para execução mensal:
    ```bash
    0 0 1 * * /usr/bin/python3 /caminho/script/question_1.py >> /caminho/log/inflation_data.log 2>&1
    ```
- Salvar e sair
- Verificar se foi criado corretamente: `crontab -l`

**Windows Task Scheduler:**
- Criar tarefa básica
- Adicionar gatilho mensal e configurar data e hora de execução do script
- Em "Iniciar um programa", no campo "Programa/script", digitar o caminho para o interpretador Python
- Em "Adicionar argumentos", digitar o caminho para o script question_1.py
- Concluir a configuração
- Verificar a execução

### Questão 4 (question_4.py):
Explicar como relacionar as séries All items e Gasoline

#### Passos:
Calculando a correlação entre as duas séries:
- Ler o arquivo inflation_data.csv
- Filtrar os dados para as duas colunas
- Calcular a correlação através da função `corr()`

### Questão bônus (bonus_question.py):
Criação de API com FastAPI para requisições dos dados armazenados no arquivo CSV.

#### Passos:
- Criação da API, com endpoint HTTP GET para as requisições
- Criação de servidor web utilizando uvicorn
