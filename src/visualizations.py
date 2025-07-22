import plotly.express as px

def grafico_producao_estado(df):
    fig = px.bar(
        df.groupby("estado")["quantidade_produzida"].sum().reset_index(),
        x="estado",
        y="quantidade_produzida",
        title="Produção por Estado",
        labels={"quantidade_produzida": "Produção (toneladas)"},
    )
    return fig

def grafico_tipo_cultura(df):
    fig = px.pie(
        df,
        names="tipo_cultura",
        values="quantidade_produzida",
        title="Distribuição por Tipo de Cultura"
    )
    return fig
