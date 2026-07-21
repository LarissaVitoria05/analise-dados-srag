import pandas as pd


def processar_dados_pe(caminho_csv):
    # Lendo apenas as colunas que realmente importam para economizar RAM
    colunas_foco = ['DT_NOTIFIC', 'SG_UF_NOT', 'ID_MUNICIP', 'CS_SEXO', 'NU_IDADE_N', 'FEBRE', 'TOSSE', 'VACINA',
                    'CLASSI_FIN', 'MORB_DESC', 'NU_NOTIFIC']

    # Carregando os dados
    df = pd.read_csv(caminho_csv, sep=';', encoding='ISO-8859-1', usecols=colunas_foco)

    # Filtrando apenas Pernambuco
    df_pe = df[df['SG_UF_NOT'] == 'PE'].copy()

    # Convertendo data para formato real
    df_pe['DT_NOTIFIC'] = pd.to_datetime(df_pe['DT_NOTIFIC'], errors='coerce')

    return df_pe

# Teste básico
# df_resumo = processar_dados_pe('../Data/INFLUD19-23-03-2026.csv')
# print(df_resumo.describe())

def limpar_demografia(df):
    # Garantir que a idade seja numérica e remover valores estranhos
    df['NU_IDADE_N'] = pd.to_numeric(df['NU_IDADE_N'], errors='coerce')
    df_limpo = df[(df['NU_IDADE_N'] >= 0) & (df['NU_IDADE_N'] <= 110)].copy()

    # Mapear o sexo para ficar mais legível no gráfico
    # M = Masculino, F = Feminino, I = Ignorado
    mapa_sexo = {'M': 'Masculino', 'F': 'Feminino', 'I': 'Não Informado'}
    df_limpo['CS_SEXO'] = df_limpo['CS_SEXO'].map(mapa_sexo)
    return df_limpo


def criar_faixas_etarias(df):
    # Criando os cortes
    bins = [0, 12, 18, 60, 110]
    labels = ['Criança (0-12)', 'Adolescente (0-17)', 'Adulto (18-59)', 'Idoso (60+)']

    # ATENÇÃO: Tire o '#' do início desta linha e feche o parêntese no final
    df['Faixa_Etaria'] = pd.cut(df['NU_IDADE_N'], bins=bins, labels=labels, right=False)

    return df