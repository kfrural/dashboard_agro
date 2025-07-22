import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from utils.utils import load_data, estados_disponiveis, filtrar_por_estado

# Carregar dados
df = load_data()

# Inicializar app Dash
app = dash.Dash(__name__)
app.title = "Dashboard Agro"

# Layout da interface
app.layout = html.Div(style={'padding': '20px'}, children=[
    html.H1("📊 Dashboard de Produção Agropecuária", style={'textAlign': 'center'}),

    html.Label("Selecione o Estado:", style={'marginTop': '20px'}),
    dcc.Dropdown(
        id='estado-dropdown',
        options=[{'label': est, 'value': est} for est in estados_disponiveis(df)],
        value=estados_disponiveis(df)[0],
        style={'width': '300px'}
    ),

    dcc.Graph(id='grafico-linha'),
    dcc.Graph(id='grafico-box'),
    dcc.Graph(id='grafico-barra')
])

# Callbacks interativos
@app.callback(
    [Output('grafico-linha', 'figure'),
     Output('grafico-box', 'figure'),
     Output('grafico-barra', 'figure')],
    [Input('estado-dropdown', 'value')]
)
def atualizar_graficos(estado_selecionado):
    df_estado = filtrar_por_estado(df, estado_selecionado)

    fig_linha = px.line(df_estado, x="ano", y="producao", title="Evolução da Produção por Ano")
    fig_box = px.box(df_estado, x="ano", y="producao", title="Distribuição de Produção")
    fig_barra = px.bar(df_estado.groupby("municipio")["producao"].sum().nlargest(10).reset_index(),
                       x="municipio", y="producao", title="Top 10 Municípios por Produção")

    return fig_linha, fig_box, fig_barra

# Executar servidor
if __name__ == '__main__':
    app.run_server(debug=True)
