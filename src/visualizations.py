import plotly.express as px

def grafico_producao_estado(df):
    fig = px.bar(
        df.groupby("estado")["producao_toneladas"].sum().reset_index(),
        x="estado",
        y="producao_toneladas",
        title="Produção por Estado",
        labels={"producao_toneladas": "Produção (toneladas)"},
    )
    return fig

def grafico_tipo_cultura(df):
    fig = px.pie(
        df,
        names="produto",
        values="producao_toneladas",
        title="Distribuição por Tipo de Cultura"
    )
    return fig
