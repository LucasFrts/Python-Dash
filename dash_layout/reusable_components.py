from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
import requests, io
def csv_factory(url):
    content = requests.get(url).content
    return pd.read_csv(io.StringIO(content.decode('UTF-8')))

url = 'https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv'
df = csv_factory(url)
url = 'https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv'
df2 = csv_factory(url)

fig = px.scatter(df2, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app = Dash(__name__)

app.layout = html.Div([
    html.H4("US Agriculture Exports (2011)"),
    generate_table(df),
    html.Div([
    dcc.Graph(id='life-exp-vs-gdp',
              figure=fig)
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)