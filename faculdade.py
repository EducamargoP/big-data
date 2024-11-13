import pandas as pd
from sqlalchemy import create_engine, text
import streamlit as st
import plotly.express as px

# 1. Criação de dados fictícios
data = {
    'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'],
    'Vendas': [250, 300, 400, 350, 500, 600],
    'Despesas': [200, 250, 300, 280, 320, 450],
    'Lucro': [50, 50, 100, 70, 180, 150]
}
df = pd.DataFrame(data)

# 2. Conecte ao banco de dados PostgreSQL
engine = create_engine('postgresql+psycopg2://eduteste:123456@localhost:5432/minha_rede')

# 3. Insira os dados no banco de dados
df.to_sql('minha-redee', engine, if_exists='replace', index=False)

# 4. Crie as views SQL
views_sql = [
    """
    CREATE VIEW view_vendas AS
    SELECT Mes, Vendas
    FROM minha-redee;
    """,
    """
    CREATE VIEW view_despesas AS
    SELECT Mes, Despesas
    FROM minha-redee;
    """,
    """
    CREATE VIEW view_lucro AS
    SELECT Mes, Lucro
    FROM minha-redee;
    """
]

with engine.connect() as connection:
    for view_sql in views_sql:
        connection.execute(text(view_sql))

# 5. Crie um dashboard Streamlit
st.title("Dashboard de Vendas - Fictício")

# Carregar dados da view de vendas
data_vendas = pd.read_sql("SELECT * FROM view_vendas", engine)
data_despesas = pd.read_sql("SELECT * FROM view_despesas", engine)
data_lucro = pd.read_sql("SELECT * FROM view_lucro", engine)

# Plotar gráficos com Plotly
fig_vendas = px.line(data_vendas, x='Mes', y='Vendas', title="Vendas por Mês")
fig_despesas = px.line(data_despesas, x='Mes', y='Despesas', title="Despesas por Mês")
fig_lucro = px.line(data_lucro, x='Mes', y='Lucro', title="Lucro por Mês")

st.plotly_chart(fig_vendas)
st.plotly_chart(fig_despesas)
st.plotly_chart(fig_lucro)

# Exibir tabelas de dados
st.write("Dados de Vendas")
st.write(data_vendas)

st.write("Dados de Despesas")
st.write(data_despesas)

st.write("Dados de Lucro")
st.write(data_lucro)



