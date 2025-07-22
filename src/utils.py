import pandas as pd

def load_data(path="data/raw/producao_agropecuaria.csv"):
    df = pd.read_csv(path)
    return df
