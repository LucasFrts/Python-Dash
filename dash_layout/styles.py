from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app = Dash(__name__)

df = pd.DataFrame({
     "Foods": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
fig = px.bar(df, x="Foods", y="Amount", color="City", barmode="group")
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(
    style={
        'backgroundColor': colors['background']
    },children=[
    html.H1(children="Hello Dash",
            style={
                'textAlign':'center',
                'color': colors['text']
            }),
    html.Div(children='''
        Dash: A web application framework for you data....
    ''',
        style={
            'textAlign':'center',
            'color':colors['text']
            
            }
    ),
    dcc.Graph(
        id="example-fraph",
        figure=fig
    )

])


if __name__ == '__main__':
    app.run(debug=True)