from waitress import serve
import sys
from dash import Dash, html, dcc, Input, Output, callback
import plotly.graph_objects as go

global settings
settings=[[0,0]]

app = Dash()

fig = go.Figure()
xmin = -10
xmax = 10
ymin = -4
ymax = 4


fig.update_layout(
    width = 629-20,
    height = 385-20,

)
xpad = (xmax-xmin)/20
ypad = (ymax-ymin)/20
fig.update_layout(xaxis=dict(range=[xmin-xpad,xmax+xpad]))
fig.update_layout(yaxis=dict(range=[ymin-ypad,ymax+ypad]))
fig.update_layout(
title=dict(
    text= "title"
),
xaxis=dict(
    title=dict(
        text="x_axis_title"
    )
),
yaxis=dict(
    title=dict(
        text="y_axis_title"
    )
)
)

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.layout.
if __name__ == '__main__':
    sevrer = serve(app, host="127.0.0.1", port=52244)
    #https://stackoverflow.com/a/133891/18535692 says should use a port between 49152 and 65535 and avoid ones used by popular apps'''
    #app.run(debug=True)
