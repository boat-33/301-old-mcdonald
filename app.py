from turtle import title
import dash
import plotly.graph_objs as go
import pandas as pd
from dash import html, Input, Output, dcc

########### Define your variables ######

# here's the list of possible columns to choose from.
list_of_columns =['total exports', 'beef', 'pork', 'poultry',
       'dairy', 'fruits fresh', 'fruits proc', 'total fruits', 'veggies fresh',
       'veggies proc', 'total veggies', 'corn', 'wheat', 'cotton']

myheading1 = 'Agricultural Exports By State'
mygraphtitle = '2011 US Agriculture Exports by State'
mycolorscale = 'ylorrd' # Note: The error message will list possible color scales.
mycolorbartitle = "Millions USD"
tabtitle = 'Agricultural Data'
sourceurl = 'https://plot.ly/python/choropleth-maps/'
githublink = 'https://github.com/boat-33/dash-map-usa-agriculture'


########## Set up the chart

import pandas as pd
df = pd.read_csv('assets/usa-2011-agriculture.csv')

# fig = go.Figure(data=go.Choropleth(
#     locations=df['code'], # Spatial coordinates
#     z = df[mycolumn].astype(float), # Data to be color-coded
#     locationmode = 'USA-states', # set of locations match entries in `locations`
#     colorscale = mycolorscale,
#     colorbar_title = mycolorbartitle,
# ))

# fig.update_layout(
#     title_text = mygraphtitle,
#     geo_scope='usa',
#     width=1200,
#     height=800
# )

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
dropdown=[]
for i in list(list_of_columns):
    dropdown.append({"label": i, "value": i})

app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div([dcc.Dropdown(dropdown, value='total exports', id='agriculture-dd')]),
    html.Div([dcc.Graph(id='agriculture-dd-container')]),
    #dcc.Graph(
    #    id='figure-1',
    #    figure=fig
    #),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Define callback as in project 3
@app.callback(Output('agriculture-dd-container', 'figure'), Input('agriculture-dd', 'value'))
def update_output(value):
    fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df[value].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = mycolorscale,
    colorbar_title = mycolorbartitle,
    ))

    mygraphtitle=f"Selected: {value}"
    
    fig.update_layout(
        geo_scope='usa',
        title=mygraphtitle,
        width=1200,
        height=800
    )
    
    return fig

############ Deploy
if __name__ == '__main__':
    app.run_server()
