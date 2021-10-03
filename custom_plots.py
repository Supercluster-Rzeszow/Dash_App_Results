import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.io as pio

import numpy as np
import pandas as pd
import plotly.express as px

# data







def force_ploting(app, data):
        available_indicators = [col for col in data.columns]

        plot_type = go.Figure()

        fig =  html.Div([
                            dbc.Row([

                                dbc.Col([
                                    dbc.Row([
                                                dbc.Col(
                                                        dcc.Dropdown(
                                                            id='crossfilter-xaxis-column',
                                                            options=[{'label': i, 'value': i} for i in available_indicators],
                                                            value='Buoyancy [N]'
                                                        ), width=10)
                                            ]),
                                    dbc.Row([
                                        dbc.Col(
                                                dbc.Row(
                                                    [
                                                        dbc.Col(dbc.Alert("X Axis options", color="#f5f5ff"), width={"size": 5, "offset": 1}),

                                                        dbc.Col(dcc.RadioItems(
                                                            id='crossfilter-xaxis-type-1',
                                                            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                                                            value='Linear',
                                                            labelStyle={'display': 'inline-block', 'marginTop': '5px'},
                                                                        ), width={"size": 3, "offset": 1})
                                                        ]),
                                                        width=5),
                                        dbc.Col(
                                            dbc.Row([
                                                    dbc.Col(dbc.Alert("Y Axis options", color="#f5f5ff"), width={"size": 5, "offset": 1}),
                                                    dbc.Col(dcc.RadioItems(
                                                        id='crossfilter-yaxis-type-1',
                                                        options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                                                        value='Linear',
                                                        labelStyle={'display': 'inline-block', 'marginTop': '5px'},
                                                                ), width={"size": 3, "offset": 1})
                                                ]),
                                                width=5),

                                    ])
                                ],
                                style={'width': '49%', 'display': 'inline-block'}),

                                dbc.Col([
                                    dbc.Row([
                                        dbc.Col(
                                            dcc.Dropdown(
                                                id='crossfilter-yaxis-column',
                                                options=[{'label': i, 'value': i} for i in available_indicators],
                                                value='Gravity [N]'
                                            ), width=5),
                                        dbc.Col(
                                            dcc.Dropdown(
                                                id='crossfilter-yaxis-column-2',
                                                options=[{'label': i, 'value': i} for i in available_indicators],
                                                value='Gravity [N]'
                                            ), width=5),
                                            ]),
                                            ])
                            ], style={
                                'padding': '10px 5px'
                            }),

                            dbc.Container([
                                            dbc.Row([
                                                        dbc.Col(
                                                                dbc.Row(
                                                                    [
                                                                    dcc.Graph(
                                                                        id='crossfilter-indicator-scatter',
                                                                        figure=plot_type,
                                                                        style = {'height': '90%', 'width':'90%'}
                                                                            )], className="h-100"
                                                                        )

                                                                ),

                                                        dbc.Col(
                                                            [
                                                            dbc.Row(dcc.Graph(id='x-time-series', figure=plot_type, style={'height': '90%','width':'90%', }), className="h-50"),
                                                            dbc.Row(dcc.Graph(id='y-time-series', figure=plot_type, style={'height': '90%','width':'90%'}), className="h-50"),
                                                            ])
                                                    ], className="h-100")
                                        ], fluid=True, style={"height": "30vh"})
            ])


        return fig

