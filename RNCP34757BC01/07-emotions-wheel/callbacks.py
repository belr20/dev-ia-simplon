from app import app

from dash.dependencies import Input, Output
from dash import dash_table

import pandas as pd
import numpy as np
import plotly.express as px

from functions import subsample, words_distribution
from sklearn.feature_extraction.text import CountVectorizer


PAGE_SIZE = 10
dfK = pd.read_csv('./data/Emotion_final.csv')
dfW = pd.read_csv('./data/text_emotion.csv')
dff = dfK[:0]

resK = pd.read_csv('./data/clf_analysis_results_K.csv')
resW = pd.read_csv('./data/clf_analysis_results_W.csv')


@app.callback(Output('app-1-display-value', 'children'),
              Input('app-1-dropdown', 'value'))
def display_data_format(value):
    if value is None:
        return 'Select data set : KAGGLE or DATA WORD ?'
    else:
        return 'You have selected {} data set'.format(value)


@app.callback(Output('table', 'data'),
              Input('app-1-dropdown', 'value'))
def update_table_data(value):
    if value == 'KAGGLE':
        dff = dfK
    elif value == 'DATA WORD':
        dff = dfW.rename(columns={
            'sentiment': 'Emotion',
            'content': 'Text'
            })
    else:
        dff = dfK[:0]
    return dff.iloc[:].to_dict('records')


@app.callback(Output('labels-distribution', 'figure'),
              Input('app-1-dropdown', 'value'))
def update_labels_distribution(value):
    if value == 'KAGGLE':
        dff = dfK
    elif value == 'DATA WORD':
        dff = dfW.rename(columns={
            'sentiment': 'Emotion',
            'content': 'Text'
            })
    else:
        dff = dfK[:0]
    fig = px.histogram(dff, x='Emotion')
    fig.update_xaxes(categoryorder="total descending")
    fig.update_layout(
        title='Emotions Histograms',
        yaxis=dict(title="Occurences"),
        xaxis=dict(title='Emotions')
        )
    return fig


@app.callback(Output('words-distribution', 'figure'),
              Input('app-1-dropdown', 'value'))
def update_words_distribution(value):
    if value == 'KAGGLE':
        dff = dfK
    elif value == 'DATA WORD':
        dff = dfW.rename(columns={
            'sentiment': 'Emotion',
            'content': 'Text'
            })
    else:
        dff = dfK[:1]

    r, freq, classes = words_distribution(dff.Text)

    # # Vectorization
    # cv = CountVectorizer()
    # X = cv.fit_transform(dff.Text)
    # # Compute rank
    # words = cv.get_feature_names()
    # wsum = np.array(X.sum(0))[0]
    # ix = wsum.argsort()[::-1]
    # wrank = wsum[ix]
    # classes = [words[i] for i in ix]
    # freq = subsample(wrank)
    # r = np.arange(len(freq))

    fig = px.bar(
        x=r,
        y=freq,
        labels={
            'x': 'Words',
            'y': 'Occurences'
        },
        title='Words Distribution with the 100 most frequent + the 10 less frequent'
    )
    fig.update_xaxes(
        tickmode='array',
        tickvals=r,
        ticktext=subsample(classes)
    )
    return fig


@app.callback(Output('app-2-display-value', 'children'),
              Input('app-2-dropdown', 'value'))
def display_data(value):
    if value is None:
        return 'Select data set : KAGGLE or DATA WORD ?'
    else:
        return 'You have selected {} data set'.format(value)


@app.callback(Output('results-display', 'children'),
              Input('app-2-dropdown', 'value'))
def update_table_analysis(value):
    if value == 'KAGGLE':
        res = resK
    elif value == 'DATA WORD':
        res = resW
    else:
        res = resK[:0]
    table = dash_table.DataTable(
        id='clf-analysis',
        columns=[{"name": i, "id": i} for i in res.columns],
        data=res.to_dict('records')
        )
    return table
