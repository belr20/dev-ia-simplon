from app import app
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


df = pd.read_csv('https://simplonline-v3-prod.s3.eu-west-3.amazonaws.com/media/file/csv/be67fa74-2c34-419c-9249-050394a7eb3e.csv')
dff = df
df = df[df.year == 2016].iloc[:50, :]
df = df.dropna()
#df.world_rank = pd.to_numeric(df.world_rank, errors='coerce')
#df2016.world_rank = [int(each.replace('=', '')) for each in df2016.world_rank]
#df2016.international_students = [str(each).replace('%', '') for each in df2016.international_students]
#df2016.rename(columns={"international_students": 'international_students_%'})
#df2016.female_male_ratio = [str(each).split() for each in df2016.female_male_ratio]
#df2016.female_male_ratio = [(float(each[0]) / float(each[2])) for each in df2016.female_male_ratio]
#df2016.female_male_ratio = pd.to_numeric(df2016.female_male_ratio, errors='coerce')

# List of operators for data table query
operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]

def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part

                # word operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value

    return [None] * 3


@app.callback(
    Output('output-state', 'children'),
    Input('upload-button', 'n_clicks'))
def update_output(n_clicks):
    return u'''The Button has been pressed {} times'''.format(n_clicks)


@app.callback(
    Output('table', "data"),
    Input('table', "page_current"),
    Input('table', "page_size"),
    Input('table', "sort_by"),
    Input('table', "filter_query"))
def update_table(page_current, page_size, sort_by, filter):
    print(filter)
    filtering_expressions = filter.split(' && ')
    dff = df
    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)

        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
            # these operators match pandas series operator method names
            dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
        elif operator == 'contains':
            dff = dff.loc[dff[col_name].str.contains(filter_value)]
        elif operator == 'datestartswith':
            # this is a simplification of the front-end filtering logic,
            # only works with complete fields in standard format
            dff = dff.loc[dff[col_name].str.startswith(filter_value)]

    if len(sort_by):
        dff = dff.sort_values(
             [col['column_id'] for col in sort_by],
             ascending=[
                 col['direction'] == 'asc'
                 for col in sort_by
                 ],
             inplace=False
        )

    page = page_current
    size = page_size
    return dff.iloc[page * size: (page + 1) * size].to_dict('records')


@app.callback(Output('app-2-display-value', 'children'),
              Input('app-2-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)
