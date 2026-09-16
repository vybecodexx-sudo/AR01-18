# ARQUIVO PRINCIPAL PARA O STREAMLIT

import pandas as pd
import streamlit as st

#importando as funções
from grafico1 import gerar_grafico_1
from grafico2 import gerar_grafico_2


st.set_page_config(page_title="Sinalização Ferroviária - Reposição", layout="wide")


st.title("Análise de Sinalização Ferroviária")


st.divider()


#leitura
df = pd.read_csv("dataset_sinalizacao_ferroviaria.csv")
df_copy = df.copy()


#primeiro gráfico exibição
st.subheader("1. Comparação de Headway por Sinalização")

col1, col2 = st.columns([2, 1])

with col1:
    fig1 = gerar_grafico_1(df_copy)
    st.pyplot(fig1)

with col2:
    st.write("Neste primeiro gráfico, observa-se claramente a diferença de desempenho entre os dois sistemas no tempo de intervalo (headway) entre as composições. A visualização do CBTC destaca uma variação de valores muito mais concentrada, demonstrando que a operação sob esse sistema se torna significativamente mais pontual, previsível e protegida contra atrasos em cadeia. Sob a ótica operacional, a transição para a tecnologia CBTC possibilita rodar mais trens por hora na mesma linha existente, elevando a capacidade de transporte sem a necessidade de investimentos em expansão de infraestrutura física.")


st.divider()


#segundo gráfico exibição
st.subheader("2. Relação entre Velocidade e Ocupação")

col3, col4 = st.columns([2, 1])

with col3:
    fig2 = gerar_grafico_2(df_copy)
    st.pyplot(fig2)

with col4:
    st.write('O segundo gráfico evidencia uma clara relação inversamente proporcional: conforme a velocidade permitida aumenta, o tempo de ocupação do trecho diminui. Isso ocorre porque, quanto mais rápido o trem percorre o circuito, menos tempo ele permanece sobre ele. Em faixas de baixa velocidade, o tempo de ocupação dispara, ressaltando o grande impacto que zonas de parada, áreas de manobra ou trechos de aproximação de estações exercem sobre a circulação. Em contrapartida, quando a velocidade se eleva, o tempo de ocupação estabiliza em patamares mínimos, garantindo que a via seja liberada rapidamente para que o próximo trem prossiga com total segurança.')