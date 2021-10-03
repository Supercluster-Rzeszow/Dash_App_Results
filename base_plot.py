def plot():
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
            size=18,
                    ),
        title={
            'text': "<b>Forces in y axis</b>",
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

    time_graph = dcc.Graph(id='graph_1',figure=time_fig)


    return time_graph