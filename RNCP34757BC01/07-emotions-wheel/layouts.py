import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd


PAGE_SIZE = 10
dfK = pd.read_csv('./data/Emotion_final.csv')
dfW = pd.read_csv('./data/text_emotion.csv')
dff = dfK[:0]

resK = pd.read_csv('./data/clf_analysis_results_K.csv')
resW = pd.read_csv('./data/clf_analysis_results_W.csv')

layoutMain = html.Div([
    html.Div(children=[
        html.H1(
            children="Emotions Wheel <3",
            style={'textAlign': 'center'}
            )
        ]),
    dcc.Link('Data Sets', href='/app1'),
    html.Br(),
    html.Br(),
    dcc.Link('Classifiers', href='/app2'),
])

layout1 = html.Div([
    html.H1(
        children='Data Sets',
        style={'textAlign': 'center'}
            ),
    html.Br(),
    dcc.Dropdown(
        id='app-1-dropdown',
        options=[
            {'label': '{}'.format(i), 'value': i} for i in [
                'KAGGLE',
                'DATA WORD'
                ]
        ]
    ),
    html.Br(),
    html.Br(),
    html.Div(id='app-1-display-value'),
    html.Br(),
    html.Br(),
    html.Div(
        dash_table.DataTable(
            id='table',
            columns=[
                {'name': i, 'id': i, "deletable": True, "selectable": True, "hideable": True}
                for i in dff.columns
            ],
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto'
            },
            style_table={
                'maxHeight': '800px',
                'overflowY': 'scroll'
            },

            editable=True,

            filter_action='native',

            sort_action='native',
            sort_mode='single',

            column_selectable="multi",
            row_selectable="multi",
            row_deletable=True,

            page_current=0,
            page_size=PAGE_SIZE,
            page_action='native'
        )
    ),
    html.Br(),
    html.Br(),
    html.Div([
        dcc.Graph(id='labels-distribution')
        ]),
    html.Div([
        dcc.Graph(id='words-distribution')
        ]),
    html.Br(),
    html.Br(),
    dcc.Link('Back to Home page', href='/'),
    html.Br(),
    html.Br(),
    dcc.Link('Go to Classifiers', href='/app2'),
    html.Br(),
    html.Br()
])

layout2 = html.Div([
    html.H1(
        children='Classifiers',
        style={'textAlign': 'center'}
            ),
    html.Br(),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': '{}'.format(i), 'value': i} for i in [
                'KAGGLE',
                'DATA WORD'
                ]
        ]
    ),
    html.Br(),
    html.Div(id='app-2-display-value'),
    html.H3(
        children='Results',
        style={'textAlign': 'center'}
    ),
    html.Br(),
    html.Div(id='results-display'),
    html.Br(),
    html.Br(),
    dcc.Link('Back to Home page', href='/'),
    html.Br(),
    html.Br(),
    dcc.Link('Go to Data Sets', href='/app1')
])
