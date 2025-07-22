import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Carrega os dados a partir de um arquivo CSV."""
    return pd.read_csv(file_path)

def check_missing_data(df: pd.DataFrame) -> pd.Series:
    """Retorna a contagem de valores ausentes por coluna."""
    return df.isnull().sum()

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Limpa os dados, removendo ou preenchendo valores faltantes e corrigindo anomalias."""
    df = df.dropna(subset=['producao_toneladas'])  # remove registros com produção ausente
    df['estado'] = df['estado'].str.upper()
    return df

def get_summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna estatísticas descritivas por produto."""
    return df.groupby('produto')['producao_toneladas'].describe()

def filter_by_state(df: pd.DataFrame, estado: str) -> pd.DataFrame:
    """Filtra os dados por estado."""
    return df[df['estado'] == estado.upper()]

def filter_by_year(df: pd.DataFrame, ano: int) -> pd.DataFrame:
    """Filtra os dados por ano."""
    return df[df['ano'] == ano]

def convert_to_tonnes(df: pd.DataFrame, column: str = 'producao_toneladas') -> pd.DataFrame:
    """Converte a produção para toneladas, se necessário (exemplo)."""
    df[column] = df[column] / 1000  # caso os dados estejam em kg
    return df
