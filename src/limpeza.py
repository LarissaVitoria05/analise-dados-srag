from pathlib import Path
import pandas as pd

#  o caminho do arquivo xlsx
BASE_DIR = Path(__file__).resolve().parent.parent
caminho_excel = BASE_DIR / "Data" / "srag_total.xlsx"

#  definindo as colunas foco do projeto
colunas_foco = [
    "uf *** contém br - cuidado ***",
    "municipio",
    "faixa etária",
    "casos",
    "obitos"
]

#  o lambda lê as planilhas do excel e transforma tudo em minúsculo
df = pd.read_excel(
    caminho_excel,
    engine="openpyxl",
    usecols=lambda col: str(col).strip().lower() in colunas_foco
)

#  normalizando os nomes em minúsculo
df.columns = df.columns.str.strip().str.lower()

#  filtrando apenas os registros em Pernambuco (PE)
coluna_uf = "uf *** contém br - cuidado ***"
df_pe = df[df[coluna_uf] == "PE"].copy()

# removendo a coluna de UF, ficando só apenas PE
df_pe = df_pe.drop(columns=[coluna_uf])

# --- resultados ---
print("--- DADOS APENAS DE PERNAMBUCO ---")
print(df_pe.head())

print(f"\nTotal de registros em PE: {len(df_pe)}")
print(f"Total de casos em PE: {df_pe['casos'].sum()}")
print(f"Total de óbitos em PE: {df_pe['obitos'].sum()}") #deixando obitos sem acento pois no arquivo está sem

def processar_dados_pe(caminho_csv):
    # lendo apenas as colunas que realmente importam para economizar RAM
    colunas_foco = ['DT_NOTIFIC', 'SG_UF_NOT', 'ID_MUNICIP', 'CS_SEXO', 'NU_IDADE_N', 'FEBRE', 'TOSSE', 'VACINA',
                    'CLASSI_FIN', 'MORB_DESC', 'NU_NOTIFIC']

    # carregando os dados
    df = pd.read_csv(caminho_csv, sep=';', encoding='ISO-8859-1', usecols=colunas_foco)

    # filtrando apenas Pernambuco
    df_pe = df[df['SG_UF_NOT'] == 'PE'].copy()

    # convertendo data para formato real
    df_pe['DT_NOTIFIC'] = pd.to_datetime(df_pe['DT_NOTIFIC'], errors='coerce')

    return df_pe

# teste básico
# df_resumo = processar_dados_pe('../Data/INFLUD19-23-03-2026.csv')
# print(df_resumo.describe())

def limpar_demografia(df):
    # garantir que a idade seja numérica e remover valores estranhos
    df['NU_IDADE_N'] = pd.to_numeric(df['NU_IDADE_N'], errors='coerce')
    df_limpo = df[(df['NU_IDADE_N'] >= 0) & (df['NU_IDADE_N'] <= 110)].copy()

    # mapear o sexo para ficar mais legível no gráfico
    # M = Masculino, F = Feminino, I = Ignorado
    mapa_sexo = {'M': 'Masculino', 'F': 'Feminino', 'I': 'Não Informado'}
    df_limpo['CS_SEXO'] = df_limpo['CS_SEXO'].map(mapa_sexo)
    return df_limpo


def criar_faixas_etarias(df):
    # criando os cortes para as faixas etárias de acordo com a OMS
    bins = [0, 12, 18, 60, 110]
    labels = ['Criança (0-12)', 'Adolescente (0-17)', 'Adulto (18-59)', 'Idoso (60+)']


    df['Faixa_Etaria'] = pd.cut(df['NU_IDADE_N'], bins=bins, labels=labels, right=False)

    return df