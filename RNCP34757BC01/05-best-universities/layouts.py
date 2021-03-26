import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import callbacks
import pandas as pd
import numpy as np

PAGE_SIZE = 10

df = pd.read_csv('https://simplonline-v3-prod.s3.eu-west-3.amazonaws.com/media/file/csv/be67fa74-2c34-419c-9249-050394a7eb3e.csv')
df = df[df.year == 2016].iloc[:50, :]
df = df.dropna()
dff = df
#df.world_rank = pd.to_numeric(df.world_rank, errors='coerce')
#df2016.world_rank = [int(each.replace('=', '')) for each in df2016.world_rank]
#df2016.international_students = [str(each).replace('%', '') for each in df2016.international_students]
#df2016.rename(columns={"international_students": 'international_students_%'})
#df2016.female_male_ratio = [str(each).split() for each in df2016.female_male_ratio]
#df2016.female_male_ratio = [(float(each[0]) / float(each[2])) for each in df2016.female_male_ratio]
#df2016.female_male_ratio = pd.to_numeric(df2016.female_male_ratio, errors='coerce')


layoutMain = html.Div([
    html.Div(children=[
        html.H1(
            children='What are the BEST universities ?',
            style={'textAlign': 'center'}
            )
        ]),
    dcc.Link('Data Set', href='/app1'),
    html.Br(),
    html.Br(),
    dcc.Link('PCA analysis', href='/app2'),
])


layout1 = html.Div([
    html.H1(
        children='Data Set',
        style={'textAlign': 'center'}
            ),
    html.Button(id='upload-button', children='Get Data Set'),
    html.Br(),
    html.Br(),
    html.Div(id='output-state'),
    html.Br(),
    html.Br(),
    html.Div(
        dash_table.DataTable(
            id='table',
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto'
            },
            style_table={
                'maxHeight': '800px',
                'overflowY': 'scroll'
            },
            columns=[
                        {'name': i, 'id': i} for i in df.columns
                    ],
            page_current=0,
            page_size=PAGE_SIZE,
            page_action='custom',

            filter_action='custom',
            filter_query='',

            sort_action='custom',
            sort_mode='multi',
            sort_by=[]
        ),
    ),
    html.Br(),
    html.Br(),
    dcc.Link('Back to Main Menu', href='/'),
    html.Br(),
    html.Br(),
    dcc.Link('Go to PCA Analysis', href='/app2')
])

layout2 = html.Div([
    html.H1(
        children='PCA Analysis',
        style={'textAlign': 'center'}
            ),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': '{}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
                ]
        ]
    ),
    html.Br(),
    html.Div(id='app-2-display-value'),
    html.Br(),
    dcc.Link('Back to Main Menu', href='/'),
    html.Br(),
    html.Br(),
    dcc.Link('Go to Data Set', href='/app1')
])
