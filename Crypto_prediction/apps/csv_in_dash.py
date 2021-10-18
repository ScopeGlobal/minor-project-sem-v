import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('data/predicted_result_rf.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="graph"),
    html.Button("Switch Axis", id='btn', n_clicks=0)
])

@app.callback(
    Output("graph", "figure"), 
    [Input("btn", "n_clicks")])
def display_graph(n_clicks):
    if n_clicks % 2 == 0:
        x, y = 'Date', 'Price'
    else:
        x, y = 'Date', 'Price'

    fig = px.line(df, x=x, y=y)    
    return fig