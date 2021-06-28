from jupyter_plotly_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output
from pymongo import MongoClient
import urllib.parse
from bson.json_util import dumps

#TODO: import for their CRUD module


# this is a juypter dash application
app = JupyterDash('ModuleFive')

# the application interfaces are declared here
# this application has two input boxes, a submit button, a horizontal line and div for output
app.layout = html.Div(
    [
        dcc.Input(
            id="input_user".format("text"),
            type="text",
            placeholder="input type {}".format("text")),
        dcc.Input(
            id="input_passwd".format("password"),
            type="password",
            placeholder="input type {}".format("password")),
        html.Button('Execute', id='submit-val', n_clicks=0),
       
    html.Hr(),
    html.Div(id="query-out"),
    #TODO: insert unique identifier code here
    ]
)

# this is area to define application responses or callback routines
# this one callback will take the entered text and if the submit button is clicked then call the
#  mongo database with the find_one query and return the result to the output div
@app.callback(
    Output("query-out", "children"),
    [Input("input_user".format("text"), "value"),
     Input("input_passwd".format("password"),"value"),
     Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('input_passwd', 'value')]
)

def cb_render(userValue,passValue,n_clicks,buttonValue):
    if n_clicks > 0:
        ###########################
        # Data Manipulation / Model
        # use CRUD module to access MongoDB
        ##########################
        username = urllib.parse.quote_plus(userValue)
        password = urllib.parse.quote_plus(passValue)
        #TODO: Instantiate CRUD object with above authentication username and password values
        main
        
        
def main():
        client = MongoClient()
        #client = MongoClient('mongodb://%s:%s@localhost:37918/AAC?authSource=AAC' % (username, password))
        client = MongoClient('mongodb://aacuser:aacuser@localhost:37918/AAC/')
        mydatabase = client['AAC']
        mycollection = mydatabase['animals']
       
        allrec = mycollection.find_one({"animal_type":"Dog","name":"Smoke"})
        for recs in allrec:
            print(allrec)
        # note that MongoDB returns BSON, the pyMongo JSON utility function dumps is used to convert to text
        #TODO: Return example query results

#cb_render
app