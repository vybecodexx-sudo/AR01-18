import matplotlib.pyplot as plt

## Boxplot: headway_seg por tipo_sinalizacao — CBTC deve mostrar headways menores ##

# Primeiro gráfico - comparação de headways - GRÁFICO DE BOXPLOT
def gerar_grafico_1(df_copy):
    #base
    fig1, ax1 = plt.subplots()

    #filtrando
    head_bloco = df_copy[df_copy['tipo_sinalizacao'] == 'Bloco Fixo']['headway_seg']
    head_cbtc = df_copy[df_copy['tipo_sinalizacao'] == 'CBTC']['headway_seg']

    #gráfico
    ax1.boxplot([head_bloco, head_cbtc], tick_labels=['Bloco Fixo', 'CBTC'])
    ax1.set_ylabel('Headway (s)')
    ax1.set_title('Comparação de Headway')
    return fig1