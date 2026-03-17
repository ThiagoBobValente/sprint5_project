# importando as bibliotecas necessárias
import pandas as pd
import plotly.express as px
import streamlit as st

# carregando o dataset
carros_dataset = pd.read_csv('./vehicles.csv')
st.header('Carros Dataset - Análise Exploratória de Dados') # adicionando um título para a aplicação

botao_histograma = st.button('Exibir Histograma de Odômetro') # adicionando um botão para exibir o histograma de odômetro

if botao_histograma:
    st.write('Exibindo o histograma para os anunciantes de carros:')
    histograma_carros = px.histogram(carros_dataset, x='odometer', title='Distribuição de Marcas de Carros')
    st.plotly_chart(histograma_carros, use_container_width=True)

# criando um botão para exibir o gráfico de dispersão entre odômetro e preço
botao_scatter = st.button('Exibir Gráfico de Dispersão entre Odômetro e Preço')

if botao_scatter:
    st.write('Exibindo o gráfico de dispersão para os anunciantes de carros:')
    scatter_carros = px.scatter(carros_dataset, x='odometer', y='price', title='Relação entre Odômetro e Preço dos Carros')
    st.plotly_chart(scatter_carros, use_container_width=True)

