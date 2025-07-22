import dash
from dash import html, dcc
from src.utils import load_data
from src.visualizations import grafico_producao_estado, grafico_tipo_cultura
# app.py


df = load_data()

app = dash.Dash(__name__)
app.title = "Dashboard Agro"

app.layout = html.Div([
    html.H1("📊 Dashboard Agropecuário Brasileiro", style={'textAlign': 'center'}),
    
    html.Div([
        dcc.Graph(figure=grafico_producao_estado(df)),
        dcc.Graph(figure=grafico_tipo_cultura(df))
    ], style={'display': 'flex', 'flexDirection': 'column', 'gap': '20px'})
])

if __name__ == '__main__':
    app.run(debug=True)

