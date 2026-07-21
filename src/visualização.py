from matplotlib import pyplot as plt


def grafico_barras_empilhadas(df):
    # Criando os dados agrupados
    dados_plot = df.groupby(['Faixa_Etaria', 'CS_SEXO'], observed=True).size().unstack().fillna(0)

    # Criando o gráfico
    ax = dados_plot.plot(kind='bar', stacked=True, figsize=(10, 6), color=['#ff9999', '#66b3ff'])

    # Adicionando os números manualmente para garantir que apareçam
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        if height > 0:  # Só desenha se o valor for maior que zero
            x, y = p.get_xy()
            ax.text(x + width / 2,
                    y + height / 2,
                    f'{int(height)}',
                    ha='center',
                    va='center',
                    fontsize=12,
                    fontweight='bold',
                    color='white')  # Branco costuma destacar melhor no azul/rosa

    plt.title('Distribuição por Faixa Etária e Sexo - PE', fontsize=14)
    plt.xlabel('Faixa Etária', fontsize=14)
    plt.ylabel('Total de Notificações', fontsize=12)
    plt.legend(title='Sexo')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()