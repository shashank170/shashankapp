
import dash_html_components as html
import dash
from subprocess import call
from dash.exceptions import PreventUpdate
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import plotly.graph_objs as go


app = dash.Dash()

app.layout = html.Div([
    #dcc.Input(id='my-id', value='initial value', type="text"),
    html.Button('Run Forcast', id='button'),
    html.H3(id='my-div'),

    
    html.Button('Run Visualisation', id='button1'),
    html.Div(id='my-div1'),
    dcc.Graph(id='graph-with-slider')
])


@app.callback(
    dash.dependencies.Output('my-div', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')]
)

def run_script_onClick(n_clicks):
    # Don't run unless the button has been pressed...
    if not n_clicks:
        raise PreventUpdate

    script_path = 'C:/Users/shashank.i.mishra/Desktop/Flask Project/Hi.py'  
    call(["python3", script_path])
    script_fn = script_path
    o=exec(open(script_fn).read())
    return o


@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),
    [dash.dependencies.Input('button1', 'n_clicks')]
)

def run_visual_onClick(n_clicks):
    # Don't run unless the button has been pressed...
    if not n_clicks:
        raise PreventUpdate
    else:
     df=pd.read_excel('C:/Users/shashank.i.mishra/Desktop/Flask Project/Forecast_Result.xlsx')
     filtered_df = df[['Week','GB']]
     data = go.Scatter(
	x=list(filtered_df.loc[:,'Week']),
	y=list(filtered_df.loc[:,'GB']),
	name='Scatter',
	mode = 'lines+markers',)

    return {
	    'data':[data]
            }

if __name__ == "__main__":
    	app.run_server(debug=False)
  