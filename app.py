import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

import numpy as np

import plotly.express as px
import pandas as pd


#Mapbox
MAPBOX_ACCESS_TOKEN = "pk.eyJ1Ijoia2FmcmFua293c2thIiwiYSI6ImNrc2VqeTJqcTB2dDQydnAyZjh0bmRydGMifQ.ZQctBHW3ZVhtb3_y02Y7dQ"
MAPBOX_STYLE = "mapbox://styles/mapbox/light-v10"



def display_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="#")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("Page 2", href="#"),
                    dbc.DropdownMenuItem("Page 3", href="#"),
                    dbc.DropdownMenuItem("Page 4", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="Mission Results",
        brand_href="#",
        color="primary",
        dark=True,
        fluid=True
    )
    return navbar

def display_map():

    map_data = [
        {
            "type": "scattermapbox",
            "lat": [0],
            "lon": [0],
            "hoverinfo": "text+lon+lat",
            "text": "Satellite Path",
            "mode": "lines",
            "line": {"width": 2, "color": "#707070"},
        },
        {
            "type": "scattermapbox",
            "lat": [0],
            "lon": [0],
            "hoverinfo": "text+lon+lat",
            "text": "Current Position",
            "mode": "markers",
            "marker": {"size": 10, "color": "#fec036"},
        },
    ]


    map_layout = {
        "mapbox": {
            "accesstoken": MAPBOX_ACCESS_TOKEN,
            "style": MAPBOX_STYLE,
            "center": {"lat": 45},
        },
        "showlegend": True,
        "autosize": True,
        "paper_bgcolor": "#1e1e1e",
        "plot_bgcolor": "#1e1e1e",
        "margin": {"t": 0, "r": 0, "b": 0, "l": 0},
    }

    map_graph = html.Div(
        id="world-map-wrapper",
        children=[
            dcc.Graph(
                id="world-map",
                figure={"data": map_data, "layout": map_layout},
                config={"displayModeBar": False, "scrollZoom": False},
            ),
        ],
    )

    return map_graph

def display_introduction():
    return dbc.Jumbotron(
                            [
                                dbc.Row([
                                            dbc.Col([
                                                        html.H4("Succesful mission?", className="display-3"),
                                                        html.P(
                                                            "Use app to analyze Your results "
                                                            "Let's explore near space!.",
                                                            className="lead",
                                                        ),
                                                        html.Hr(className="my-2"),
                                                        html.P(
                                                            "You can use our sample data to explore near space mission "
                                                            "or import Your own data to make impressive visualisations."
                                                        ),
                                                        html.P(dbc.Button("Learn more", color="primary"), className="lead"),], width=8),
                                            dbc.Col([
                                                    dbc.Button("Import Your data", className="fa fa-send"),
                                            ], width={"size": 2, "order": "last", "offset": 0}),
                                        ])

                            ],
                       )

def force_section():
    return dbc.Jumbotron([
                            dbc.Row([
                                    dbc.Col(
                                        [
                                            html.H4("Force exploration", className="display-3"),
                                            html.P(
                                                "Use app to analyze Your results "
                                                "Let's explore near space!.",
                                                className="lead"
                                            )
                                        ],
                                        width=6, style={'border-right': '1px solid'}
                                    ),
                                    dbc.Col(
                                        html.P(
                                            "Forces sensed with flight computer during whole flight",
                                            className="lead",
                                        ), width=5
                                    )
                                    ])
                    ])

def flight_cards():
    cards = [
        dbc.Card(
            [
                html.H2(f"26.1 km", className="display-4"),
                html.P("Maximum flight height", className="card-text"),
            ],
            body=True,
            color="light",
        ),
        dbc.Card(
            [
                html.H2(f"3.6 m/s", className="display-4"),
                html.P("Maximum speed", className="card-text"),
            ],
            body=True,
            color="dark",
            inverse=True,
        ),
        dbc.Card(
            [
                html.H2(f"12 h 6 m ", className="display-4"),
                html.P("Total flight time", className="card-text"),
            ],
            body=True,
            color="primary",
            inverse=True,
        ),
    ]
    return [dbc.Col(card, width={'size': 3, 'offset-right': 1 }) for card in cards]

def flight_detail_section():
    return dbc.Jumbotron([
                            dbc.Row([
                                    dbc.Col(
                                        [
                                            html.H4("Flight detail", className="display-3"),
                                            html.P(
                                                "Use app to compare predicted flight path with the real data",
                                                className="lead"
                                            )
                                        ],
                                        width=6, style={'border-right': '1px solid'}
                                    ),
                                    dbc.Col(
                                        html.P(
                                            "Predicting flight path is a difficult task.",
                                            className="lead",
                                        ), width=5
                                    )
                                    ])
                    ])

def design_examination_section():
    return dbc.Jumbotron([
                            dbc.Row([
                                    dbc.Col(
                                        [
                                            html.H4("Design examination", className="display-3"),
                                            html.P(
                                                "Use app to compare predicted flight path with the real data",
                                                className="lead"
                                            )
                                        ],
                                        width=6, style={'border-right': '1px solid'}
                                    ),
                                    dbc.Col(
                                        html.P(
                                            "Predicting flight path is a difficult task.",
                                            className="lead",
                                        ), width=5
                                    )
                                    ])
                    ])


def force_plots():
    # generate 100 multivariate normal samples
    data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 100)
    F_G = x=[0,1, 2, 3]
    flight_time = [0,1,2,3]
    force_fig_1 = px.line(x=flight_time, y=F_G)


    scatter = go.Figure(
        data=[go.Scatter(x=data[:, 0], y=data[:, 1], mode="markers")]
    )

    # time
    time_fig = go.Figure()

    time_fig.add_trace(go.Scatter(
        x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        y=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        name="Predicted"  # this sets its legend entry
    ))

    time_fig.add_trace(go.Scatter(
        x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        y=[1, 0, 3, 2, 5, 4, 7, 6, 8],
        name="Measured"
    ))

    time_fig.update_layout(
        xaxis_title="Force [N]",
        yaxis_title="Time [s]",
        legend_title="Legend",
        font=dict(
            size=24,
        ),
        title={
            'text': "Forces in y axis",
            'y':0.9,
            'x':0.4,
            'xanchor': 'center',
            'yanchor': 'top'}
    )

    time_graph = dcc.Graph(id='graph_1',figure=time_fig,)



    plot = dbc.Container(
                            [
                                dbc.Row([
                                            dbc.Col([
                                                        dbc.Row([
                                                            dbc.Col(dcc.Graph(id='example-graph_1',figure=scatter)),
                                                            dbc.Col(dcc.Graph(id='example-graph_2', figure=scatter)),
                                                                ]),
                                                        dbc.Row([
                                                            dbc.Col(dcc.Graph(id='example-graph_3', figure=scatter)),
                                                                dbc.Col(dcc.Graph(id='example-graph_4', figure=scatter)),
                                                            ]),
                                                    ])
                                        ])
                                    ])
    return time_graph



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = html.Div([
                            dbc.Container(children=[
                                                               dbc.Row(dbc.Col(display_navbar(), width=12)),
                                                               dbc.Row(dbc.Col(display_introduction(), width=12)),
                                                               dbc.Row([dbc.Col(dbc.Jumbotron(html.H4('1', className="display-2")), width=2),dbc.Col(flight_detail_section(), width=10)]),
                                                               dbc.Row(flight_cards(), style={'margin-bottom': '30px'}, justify="center"),
                                                               dbc.Row(dbc.Col(display_map(), width=12), style={'margin-bottom': '30px'}),
                                                               dbc.Row([dbc.Col(dbc.Jumbotron(html.H4('2', className="display-2")), width=2), dbc.Col(force_section(), width=10)]),
                                                               dbc.Row(dbc.Col(force_plots(), width=8)),
                                                               dbc.Row([dbc.Col(dbc.Jumbotron(html.H4('3', className="display-2")), width=2), dbc.Col(design_examination_section(), width=10)]),
                                                            ],
                                          fluid=True)
                        ])



