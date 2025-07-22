import pandas as pd

def load_data(path="data/producao_agropecuaria_100k.csv"):
    df = pd.read_csv(path)
    df['ano'] = df['ano'].astype(int)
    df['producao'] = pd.to_numeric(df['producao'], errors='coerce')
    return df

def resumo_estatistico(df):
    return df.describe(include='all')

def estados_disponiveis(df):
    return df['estado'].unique()

def filtrar_por_estado(df, estado):
    return df[df['estado'] == estado]
