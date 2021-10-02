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

def add_plots():
    # generate 100 multivariate normal samples
    data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 100)

    scatter = go.Figure(
        data=[go.Scatter(x=data[:, 0], y=data[:, 1], mode="markers")]
    )

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
    return plot



app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
                            dbc.Container(children=[
                                                               dbc.Row(dbc.Col(display_navbar(), width=12)),
                                                               dbc.Row(dbc.Col(display_introduction(), width=12)),
                                                               dbc.Row(dbc.Col(display_map(), width=12)),
                                                               dbc.Row(dbc.Col(add_plots(), width={"size": 8, "order": 1, "offset": 0}),  justify="left")
                                                            ],
                                          fluid=True)
                        ])



if __name__ == '__main__':
    app.run_server(debug=True)