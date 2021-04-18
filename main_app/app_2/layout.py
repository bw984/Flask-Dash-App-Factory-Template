import dash_core_components as dcc
import dash_html_components as html
from main_app.dash_shared import shared_dash_nav_links

layout = html.Div([
    shared_dash_nav_links(),
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div(["Input: ",
              dcc.Input(id='my-input', value='initial value', type='text')]),
    html.Br(),
    html.Div(id='my-output'),
])
