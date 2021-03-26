import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from layouts import layoutMain, layout1, layout2
import callbacks


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # content will be rendered in this element
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
    app.run_server(host='127.0.0.1', port='8080', debug=True)
