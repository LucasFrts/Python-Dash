from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-1', type='text', value='Montréal'),
    dcc.Input(id='input-2', type='text', value='Canadá'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='number-output'),
])


@app.callback(
    Output("number-output", "children"),
    Input("submit-button-state", 'n_clicks'),
    State("input-1", "value"),
    State("input-2", "value"),
)
def update_output(clicks, input1, input2):
    return f'''
        The button has ben pressed {clicks} times,
        Input 1 is {input1},
        Intut 2 is {input2}
    '''


if __name__ == '__main__':
    app.run_server(debug=True)