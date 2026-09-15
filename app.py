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

st.markdown("Nesse gráfico podemos observar a diferença entre o headway(tempo de intervalo) de bloco fixo e o CBTC." \
"Principais pontos" \
"O gráfico que mostra o CBTC possui uma variação bem mais cocnentrada dos valores indicando que o serviço será mais pontual, previsível e com menos atrasos." \
"A troca para o CBTC permite rodas mais trens por hora na mesma linha, sem custos com expansão de infraestrutura. ")

#segundo gráfico exibição
st.subheader("2. Relação entre Velocidade e Ocupação")
fig2 = gerar_grafico_2(df_copy)
st.pyplot(fig2)

st.markdown('Nesse gráfico é perceptivel a relação inversamente proporcional onde com maior velocidade o tempo de ocupação diminui já que quanto mais rápido o trem terminar o circuito menos tempo ele vai estar ocupando o mesmo.' \
'Principais pontos:' \
'Durante baixas velocidades o tempo de ocupação dispara, isso evidencia o impacto que as zonas de parada tem, manobra ou aproximação de estações para as trocas.' \
'Em velocidades mais altas o tempo de ocupação estabiliza nos níveis mínimos, isso garante qeu o trecho fique livre mais rapidamente para o trem seguinte prosseguir de forma segura.')