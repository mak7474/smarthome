import pathlib
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app_path = str(pathlib.Path(__file__).parent.resolve())
df = pd.read_csv(os.path.join(app_path, os.path.join("data", "pokazaniya.csv")))

app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

theme = {
    'background': '#111111',
    'text': '#7FDBFF'
}


def build_banner():
    return html.Div(
        className='col-sm-10 row banner',
        children=[
            html.Div(
                className='banner-text',
                children=[
                    html.H5('Gyroscope data'),
                ],
            ),
        ],
    )


def build_graph():
    return dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df['Batch'][:50],
                    'y': df['acc_x'][:50],
                    'name': 'acc_x',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['acc_y'][:50],
                    'name': 'acc_y',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['acc_z'][:50],
                    'name': 'acc_z',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['gyro_x'][:50],
                    'name': 'gyro_x',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['gyro_y'][:50],
                    'name': 'gyro_y',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['gyro_z'][:50],
                    'name': 'gyro_z',
                    'marker': {'size': 12}
                },
            ],
            'layout': {
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],
                'font': {
                    'color': theme['text']
                }
            }
        }
    )


app.layout = html.Div(
    className='big-app-container',
    children=[
        build_banner(),
        html.Div(
            className='app-container',
            children=[
                build_graph(),
            ]
        )
    ]
)
