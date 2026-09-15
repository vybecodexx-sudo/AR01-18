import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('dataset_sinalizacao_ferroviaria.csv')

df_copy = df.copy()



## Dispersão: velocidade_permitida_kmh x tempo_ocupacao_circuito_seg — relação inversa esperada ##

# Segundo gráfico - Relação velocidade x Tempo de ocupação - GRÁFICO DE DISPERSÃO


#base
fig2, ax2 = plt.subplots()

#filtrando
ax2.scatter(df_copy['velocidade_permitida_kmh'], df_copy['tempo_ocupacao_circuito_seg'])

#gráfico
ax2.set_xlabel('Velocidade Permitida (km/h)')
ax2.set_ylabel('Tempo de Ocupação (s)')
ax2.set_title('Relação velocidade x Tempo de ocupação')
plt.show()