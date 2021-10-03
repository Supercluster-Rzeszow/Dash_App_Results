import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.io as pio

import numpy as np
import pandas as pd
import plotly.express as px

import StandardAtmosphere
# data







def force_ploting(app, data):
        available_indicators = [col for col in data.columns]

        plot_type = go.Figure()

        fig =  html.Div([
                            html.Div([

                                html.Div([
                                    dcc.Dropdown(
                                        id='crossfilter-xaxis-column',
                                        options=[{'label': i, 'value': i} for i in available_indicators],
                                        value='Czas [s]'
                                    ),
                                    dcc.RadioItems(
                                        id='crossfilter-xaxis-type',
                                        options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                                        value='Linear',
                                        labelStyle={'display': 'inline-block', 'marginTop': '5px'}
                                    )
                                ],
                                style={'width': '49%', 'display': 'inline-block'}),

                                html.Div([
                                    dcc.Dropdown(
                                        id='crossfilter-yaxis-column',
                                        options=[{'label': i, 'value': i} for i in available_indicators],
                                        value='Czas [s]'
                                    ),
                                    dcc.RadioItems(
                                        id='crossfilter-yaxis-type',
                                        options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                                        value='Linear',
                                        labelStyle={'display': 'inline-block', 'marginTop': '5px'},
                                    )
                                ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
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

