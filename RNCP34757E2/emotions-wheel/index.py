#!/bin/python
# import sys

from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app
from app import server
from layouts import layoutMain, layout1, layout2
import callbacks

# print('Python %s on %s' % (sys.version, sys.platform))
#
# sys.path.extend(['/mnt/288C64701B0AF22A/GitHub/dev-ia-simplon/RNCP34757BC01/07-emotions-wheel'])
# print("\nPATH =")
# for item in sys.path:
#     print("\t", item)
# print("=" * 120)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
    ])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/app1':
        return layout1
    elif pathname == '/app2':
        return layout2
    else:
        return layoutMain


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port='8383', debug=True)
