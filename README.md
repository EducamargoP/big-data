# big-data
 Projeto de Pipeline de Dados IoT

## Descrição do Projeto
Este projeto implementa um pipeline de dados para processar leituras de temperatura de dispositivos IoT, utilizando Python, PostgreSQL e Streamlit. Ele lê dados de um arquivo CSV, insere os dados em um banco de dados PostgreSQL, cria views SQL para análise e apresenta um dashboard interativo usando Streamlit.

## Configuração do Ambiente
1. **Instale o Python**: Baixe e instale a versão mais recente do [Python](https://www.python.org/downloads/).
2. **Instale o Docker**: Baixe e instale o [Docker](https://www.docker.com/get-started).
3. **Crie um ambiente virtual Python**:
    ```bash
    python -m venv meu_ambiente
    source meu_ambiente/bin/activate  # No Windows use: meu_ambiente\Scripts\activate
    ```
4. **Instale as bibliotecas necessárias**:
    ```bash
    pip install pandas psycopg2-binary sqlalchemy streamlit plotly
    ```

## Criação do Contêiner PostgreSQL
1. Execute o seguinte comando para criar o contêiner PostgreSQL:
    ```bash
    docker run --name postgres-iot -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres
    ```

## Desenvolvimento da Aplicação Python
1. **Crie um script Python para ler o arquivo CSV**:
    ```python
    import pandas as pd
    df = pd.read_csv('/Download/archive.csv')
    ```

2. **Utilize SQLAlchemy para conectar ao PostgreSQL**:
    ```python
    from sqlalchemy import create_engine
    engine = create_engine('postgresql+psycopg2://eduteste:123456@localhost:5432/minha_rede')
    ```

3. **Implemente a lógica para processar e inserir os dados no banco**:
    ```python
    df.to_sql('minha-redee', engine, if_exists='replace', index=False)
    ```

4. **Crie as views SQL**:
    ```sql
    CREATE VIEW view_exemplo_1 AS
    SELECT coluna1, coluna2, SUM(coluna3) AS soma_coluna3
    FROM minha-redee
    GROUP BY coluna1, coluna2;
    ```

5. **Execute o dashboard Streamlit**:
    ```python
    import streamlit as st
    import plotly.express as px

    st.title("Dashboard de Leitura de Temperatura - IoT Devices")
    
    data_query = text("SELECT * FROM view_exemplo_1")
    data = pd.read_sql(data_query, engine)
    
    fig = px.bar(data, x='coluna1', y='soma_coluna3', color='coluna2', title="Exemplo de Gráfico de Barras")
    st.plotly_chart(fig)
    
    st.write(data)
   

## Explicação das Views SQL
- **view_exemplo_1**: Soma os valores da coluna3, agrupados por coluna1 e coluna2.
- **view_exemplo_2**: Calcula a média dos valores da coluna4, agrupados por coluna1.
- **view_exemplo_3**: Conta o número de ocorrências em coluna5.

## Possíveis Insights
- A **view_exemplo_1** pode ajudar a identificar quais combinações de coluna1 e coluna2 têm os maiores valores somados de coluna3.
- A **view_exemplo_2** pode ser usada para determinar as médias de valores em coluna4 agrupados por coluna1.
- A **view_exemplo_3** pode mostrar a frequência de valores em coluna5, ajudando a identificar os valores mais comuns.
