# ARQUIVO PRINCIPAL PARA O STREAMLIT

import pandas as pd
import streamlit as st

#importando as funções
from grafico1 import gerar_grafico_1
from grafico2 import gerar_grafico_2

st.title("Análise de Sinalização Ferroviária")


#leitura
df = pd.read_csv("dataset_sinalizacao_ferroviaria.csv")
df_copy = df.copy()


#primeiro gráfico exibição
st.subheader("1. Comparação de Headway por Sinalização")
fig1 = gerar_grafico_1(df_copy)
st.pyplot(fig1)

#segundo gráfico exibição
st.subheader("2. Relação entre Velocidade e Ocupação")
fig2 = gerar_grafico_2(df_copy)
st.pyplot(fig2)