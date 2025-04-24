import pandas as pd
import streamlit as st
import joblib
import os

# Caminhos dos arquivos
caminho_base = os.path.dirname(__file__)
caminho_dados = os.path.join(caminho_base, 'dados.csv')
caminho_modelo = os.path.join(caminho_base, 'modelo.joblib')

# Features numéricas
x_numericos = {
    'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0,
    'bedrooms': 0, 'beds': 0, 'extra_people': 0, 'minimum_nights': 0,
    'ano': 0, 'mes': 0, 'N_amenities': 0, 'host_listings_count': 0,
    'number_of_reviews': 0
}

# Features booleanas (sim/não)
x_tf = ['host_is_superhost', 'instant_bookable', 'is_business_travel_ready']

# Categorias com dummies
x_listas = {
    'property_type': [
        'Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite',
        'Guesthouse', 'Hostel', 'House', 'Loft', 'Serviced apartment', 'Outros'
    ],
    'room_type': [
        'Entire home/apt', 'Hotel room', 'Private room', 'Shared room'
    ],
    'cancellation_policy': [
        'flexible', 'moderate', 'strict', 'strict_14_with_grace_period'
    ],
    'bed_type': ['Real Bed', 'Others Bed']
}

# Monta o dicionário com todos os campos
dicionario = {}

# Campos numéricos
for item in x_numericos:
    if item in ['latitude', 'longitude']:
        valor = st.number_input(f'{item}', step=0.00001, value=0.0, format='%.5f')
    elif item == 'extra_people':
        valor = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        valor = st.number_input(f'{item}', step=1, value=0)
    dicionario[item] = valor

# Campos booleanos
for item in x_tf:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    dicionario[item] = 1 if valor == 'Sim' else 0

# Categorias
for item in x_listas:
    valor = st.selectbox(f'{item}', x_listas[item])
    for categoria in x_listas[item]:
        dicionario[f'{item}_{categoria}'] = 1 if valor == categoria else 0

# Botão de previsão
botao = st.button('Prever valor do imóvel')

if botao:
    valores_x = pd.DataFrame(dicionario, index=[0])

    # Garantir que todas as colunas estejam presentes
    dados = pd.read_csv(caminho_dados)
    colunas = list(dados.columns)
    if 'price' in colunas:
        colunas.remove('price')  # remove a variável alvo
    for coluna in colunas:
        if coluna not in valores_x.columns:
            valores_x[coluna] = 0

    valores_x = valores_x[colunas]

    # Carregar modelo e prever
    modelo = joblib.load(caminho_modelo)
    preco = modelo.predict(valores_x)
    st.write(f'📍 Preço estimado da diária: **R$ {preco[0]:,.2f}**')
