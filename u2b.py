# -*- coding: utf-8 -*-
"""u2b.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1huA28LiSR3G6SFFy2bWMZ7d7Zhn7q3eL
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://github.com/arewelearningyet/DS-Unit-2-Build/blob/master/df?raw=true')

available_areas = df['area'].unique()
available_groups= df['group'].unique()

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_areas],
                value='Texas\'s 23rd congressional district'
            ),
#            dcc.RadioItems(
#                id='xaxis-type',
#                options=[{'label': i, 'value': i} for i in ['', 'Log']],
#                value='Linear',
#                labelStyle={'display': 'inline-block'}
#            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_groups],
                value='Democrat'
            ),
            # dcc.RadioItems(
            #     id='yaxis-type',
            #     options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
            #     value='Linear',
            #     labelStyle={'display': 'inline-block'}
            # )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

    dcc.Slider(
        id='term--slider',
        min=df['term'].min(),
        max=df['term'].max(),
        value=df['term'].max(),
        marks={str(term): str(term) for term in df['term'].unique()},
        step=None
    )
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),
#     Input('xaxis-type', 'value'),
#     Input('yaxis-type', 'value'),
     Input('term--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
#                 xaxis_type, yaxis_type,
                 term_value):
    dff = df[df['term'] == term_value]

    return {
        'data': [dict(
            x=dff[dff['area'] == xaxis_column_name]['gender'],
            y=dff[dff['group'] == yaxis_column_name]['gender'],
#            text=dff[dff['Indicator Name'] == yaxis_column_name]['group'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': dict(
            xaxis={
                'title': xaxis_column_name,
                'type': 'linear' #if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name,
                'type': 'linear' #if yaxis_type == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)