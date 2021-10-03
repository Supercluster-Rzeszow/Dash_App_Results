import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.io as pio
import datetime
import numpy as np

import plotly.express as px
import pandas as pd

from custom_plots import force_ploting

import Balloon_Calc_v1
import math

#Mapbox
MAPBOX_ACCESS_TOKEN = "pk.eyJ1Ijoia2FmcmFua293c2thIiwiYSI6ImNrc2VqeTJqcTB2dDQydnAyZjh0bmRydGMifQ.ZQctBHW3ZVhtb3_y02Y7dQ"
MAPBOX_STYLE = "mapbox://styles/mapbox/light-v10"


data, pop_time, pop_height, north_velocity, east_velocity = Balloon_Calc_v1.run()
df = data


def display_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("by SuperClaster", href="#")),
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
        color="#010483",
        dark=True,
        fluid=True
    )
    return navbar

def display_map():

    map_data = [
        {
            "type": "scattermapbox",
            "lat": df['Latitude [deg]'],
            "lon": df['Longitude [deg]'],
            "hoverinfo": "text+lon+lat",
            "text": "Baloon Predicted Flight Path",
            "mode": "lines",
            "line": {"width": 2, "color": "#707070"},
        },

        {
            "type": "scattermapbox",
            "lat": df['Latitude [deg]'][0],
            "lon": df['Latitude [deg]'][0],
            "hoverinfo": "text+lon+lat",
            "text": "Mission Radius",
            "mode": "markers",
            "marker": {"size": 10, "color": "#fec036"},
        },

    ]


    map_layout = {
        "mapbox": {
            "accesstoken": MAPBOX_ACCESS_TOKEN,
            "style": MAPBOX_STYLE,
            "center": {"lat": df['Latitude [deg]'][0], "lon": df['Latitude [deg]'][0]},
            "zoom": 8
        },
        "showlegend": True,
        "autosize": True,
        "paper_bgcolor": "#1e1e1e",
        "plot_bgcolor": "#1e1e1e",
        "margin": {"t": 0, "r": 0, "b": 0, "l": 0},
        "legend": {"font": {"family": "sans-serif", "size":18, "color":"white"}, }

    }


    map_graph = html.Div(
        id="world-map-wrapper",
        children=[
            dcc.Graph(
                id="world-map",
                figure={"data": map_data, "layout": map_layout},
                config={"displayModeBar": True, "scrollZoom": True},
                style={'height': '100%'}
            ),
        ], style={'height': '100%'}
    )

    return map_graph

def display_introduction():
    return dbc.Jumbotron(
                            [
                                dbc.Row([
                                            dbc.Col([
                                                        html.H4("Succesful mission?", className="h1"),
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
                                                        html.P(dbc.Button("Learn more", color="#010483"), className="lead"),], width=8),
                                            dbc.Col([
                                                    dbc.Button("Import Your data", className="fa fa-send"),
                                            ], width={"size": 2, "order": "last", "offset": 0}),
                                        ])

                            ], style={'border-bottom-radius': '30px', 'background-color': '#f5f5ff'}
                       )

def force_section():
    return dbc.Jumbotron([
                            dbc.Row([
                                    dbc.Col(
                                        [
                                            html.H4("Force exploration", className="h1"),
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
                    ], style={'border-radius': '30px', 'background-color': '#f5f5ff'})


def flight_cards():
    time_m, time_s = divmod(int(max(data["Time [s]"])), 60)
    time_h, time_m = divmod(time_m, 60)
    flight_time = str(f'{time_h:d}h:{time_m:02d}m:{time_s:02d}s')
    max_speed = max(data["Vertical speed [m/s]"])
    cards = [
        dbc.Card(
            [
                html.H2(f"{round(pop_height/1000,2)} km", className="h1"),
                html.P("Maximum flight height", className="card-text"),
            ],
            body=True,
            color='#f5f5ff',
            style={'border-radius': '10px'}
        ),
        dbc.Card(
            [
                html.H2(f"{round(max_speed,2)} m/s", className="h1"),
                html.P("Maximum speed", className="card-text"),
            ],
            body=True,
            color="dark",
            inverse=True,
            style={'border-radius': '10px'}
        ),
        dbc.Card(
            [
                html.H2(f"{flight_time} ", className="h1"),
                html.P("Total flight time", className="card-text"),
            ],
            body=True,
            color="#010483",
            inverse=True,
            style={'border-radius': '10px'}
        ),
    ]
    return [dbc.Col(card, width={'size': 3, 'offset-right': 1 }) for card in cards]


def flight_detail_section():
    return dbc.Jumbotron([
                            dbc.Row([
                                    dbc.Col(
                                        [
                                            html.H4("Flight detail", className="h1"),
                                            html.P(
                                                "Use app to compare predicted flight path with the real data",
                                                className="lead"
                                            )
                                        ],
                                        width=6, style={'border-right': '1px solid'}
                                    ),
                                    dbc.Col(
                                        html.P(
                                            "Predicting the route of the balloon is the beginning of every mission."
                                            "It allows you to make sure your planned route is safe for your payload and environment.",
                                            className="lead",
                                        ), width=5
                                    )
                                    ])
                    ], style={'border-radius': '30px', 'background-color': '#f5f5ff'})


def design_examination_section():
    return dbc.Jumbotron([
                            dbc.Row([
                                    dbc.Col(
                                        [
                                            html.H4("Design examination", className="h1"),
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
                    ], style={'border-radius': '30px', 'background-color': '#f5f5ff'})


def force_plots(df):
    # generate 100 multivariate normal samples
    data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 100)
    F_G = x=[0,1, 2, 3]
    flight_time = [0,1,2,3]
    force_fig_1 = px.line(x=flight_time, y=F_G, template="none")


    scatter = go.Figure(
        data=[go.Scatter(x=data[:, 0], y=data[:, 1], mode="markers")]
    )

    # time
    time_fig = go.Figure()

    time_fig.add_trace(go.Scatter(
        x=df['Time [s]'],
        y=df['Buoyancy Measured [N]'],
        name="Predicted"  # this sets its legend entry
    ))

    time_fig.add_trace(go.Scatter(
        x=df['Time [s]'],
        y=df['Buoyancy [N]'],
        name="Measured"
    ))

    time_fig.update_layout(
        xaxis_title="Buoyancy [N]",
        yaxis_title="Time [s]",
        legend_title="Legend",
        font=dict(
            size=18,
                    ),
        title={
            'text': "<b>Buoyancy Measured vs Predicted</b>",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        template ='none',

    )

    time_fig.update_layout(
        {'plot_bgcolor': '#f5f5ff'})

    time_fig.update_layout(
        title_font_family="Open Sans, sans-serif",
        title_font_size=24,
        font_family="Open Sans, sans-serif",
        paper_bgcolor='#f5f5ff',

                        )

    time_graph = dcc.Graph(id='graph_1',figure=time_fig, style={'height': '100%'})


    return time_graph

def measure_info():

           return dbc.Jumbotron([

                        html.H4("Why do measurements go up and down?", className="h2"),
                        html.P(
                            "The collected data will never be a straight line - if this is the case, it means that your sensor "
                            "has too low resolution! Noise is caused by many conditions - it is caused primarily by local "
                            "disturbances of the measured values, such as vibrations in the case of accelerometers or "
                            "gusts of air in the case of pressure measurements. Noise can also be created by the power"
                            "supply to the sensor. Nature is unpredictable - but we can tame these deviations with"
                            "statistics and signal filtering.",
                            className="lead",
                            style={'textAlign': 'left'}
                        )
                    ], style={'background-color': '#f5f5ff'})




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server


app.layout = html.Div([
                            dbc.Container(children=[
                                                               dbc.Row(dbc.Col(display_navbar(), width=12)),
                                                               dbc.Row(dbc.Col(display_introduction(), width=12)),
                                                               dbc.Row([dbc.Col(dbc.Jumbotron(html.H2('1', className="display-3", style={'textAlign': 'center'}), style={'border-radius': '30px', 'background-color': '#f5f5ff'}), width=2),dbc.Col(flight_detail_section(), width=10)]),
                                                               dbc.Row(flight_cards(), style={'margin-bottom': '30px'}, justify="center"),
                                                               dbc.Row(dbc.Col(display_map(), width=12, style={'height': '100%'}), style={'margin-bottom': '30px'}, className="h-40",),
                                                               dbc.Row([dbc.Col(dbc.Jumbotron(html.H2('2', className="display-3", style={'textAlign': 'center'}), style={'border-radius': '30px', 'background-color': '#f5f5ff'}), width=2), dbc.Col(force_section(), width=10)]),
                                                               dbc.Row([dbc.Col(force_plots(df),width=7), dbc.Col(measure_info(),width=4)], style={'margin-bottom': '30px'}, className="h-40"),
                                                               dbc.Row([dbc.Col(dbc.Jumbotron(html.H2('3', className="display-3", style={'textAlign': 'center'}), style={'border-radius': '30px', 'background-color': '#f5f5ff'}), width=2), dbc.Col(design_examination_section(), width=10)]),
                                                               dbc.Row(dbc.Col(force_ploting(app, data), width=12, style={'height': '100%'}), className="h-40",)
                                                            ],
                                          fluid=True, style={"height": "100vh"})
                        ])

#callbacks

@app.callback(
    dash.dependencies.Output('crossfilter-indicator-scatter', 'figure'),
    [dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-xaxis-type-1', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-type-1', 'value'),])
def update_graph(xaxis_column_name,
                 xaxis_type, yaxis_type):
    dff = df

    fig = go.Figure()

    fig.update_layout(
        {'plot_bgcolor': '#f5f5ff'})

    fig.update_layout(
        title_font_family="Open Sans, sans-serif",
        title_font_size=24,
        font_family="Open Sans, sans-serif",
        paper_bgcolor='#f5f5ff',
        template='none',
        margin={'l': 50, 'b': 50, 't': 50, 'r': 50},
    )

    fig.add_trace(go.Scatter(x=dff['Time [s]'], y=dff[xaxis_column_name] ))

    fig.update_xaxes(title='Time [s]', type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=xaxis_column_name, type='linear' if yaxis_type == 'Linear' else 'log')

    fig.update_layout(hovermode='closest')

    return fig

@app.callback(
    dash.dependencies.Output('x-time-series', 'figure'),
    [
     dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-xaxis-type-1', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-type-1', 'value'),])
def update_graph(yaxis_column_name,
                 xaxis_type, yaxis_type):
    dff = df

    fig = go.Figure()

    fig.update_layout(
        {'plot_bgcolor': '#f5f5ff'})

    fig.update_layout(
        title_font_family="Open Sans, sans-serif",
        title_font_size=24,
        font_family="Open Sans, sans-serif",
        paper_bgcolor='#f5f5ff',
        template='none',
        margin={'l': 50, 'b': 50, 't': 50, 'r': 50},
    )

    fig.add_trace(go.Scatter(x=dff['Time [s]'], y=dff[yaxis_column_name] ))

    fig.update_xaxes(title='Time [s]', type='linear' )

    fig.update_yaxes(title=yaxis_column_name, type='linear')

    fig.update_layout(hovermode='closest')

    return fig

@app.callback(
    dash.dependencies.Output('y-time-series', 'figure'),
    [
     dash.dependencies.Input('crossfilter-yaxis-column-2', 'value'),
     dash.dependencies.Input('crossfilter-xaxis-type-1', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-type-1', 'value'),])
def update_graph(yaxis_column_name,
                 xaxis_type, yaxis_type):
    dff = df

    fig = go.Figure()

    fig.update_layout(
        {'plot_bgcolor': '#f5f5ff'})

    fig.update_layout(
        title_font_family="Open Sans, sans-serif",
        title_font_size=24,
        font_family="Open Sans, sans-serif",
        paper_bgcolor='#f5f5ff',
        template='none',
        margin={'l': 50, 'b': 50, 't': 50, 'r': 50},
    )

    fig.add_trace(go.Scatter(x=dff['Time [s]'], y=dff[yaxis_column_name] ))

    fig.update_xaxes(title='Time [s]', type='linear')

    fig.update_yaxes(title=yaxis_column_name, type='linear')

    fig.update_layout(hovermode='closest')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)