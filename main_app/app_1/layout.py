import dash_core_components as dcc
import dash_html_components as html
from .data.data import Data

df = Data.get_raw()
available_indicators = Data.get_available_indicators(df)

APP_BUTTON_COLOR = '#e3e3e3'
APP_TEAL = '#05929f'

tabs_row_1_style = {
    'height': '35px',
    'marginLeft': '-8px',
    'marginTop': '-8px',
    'marginRight': '-8px',
    'marginBottom': '10px',
    'width': '100vw',
}

tab_on_row_1_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_on_row_1_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': APP_BUTTON_COLOR,
    'color': APP_TEAL,
    'padding': '6px',
    'textDecoration': 'underline',
    'fontWeight': 'bold'
}


def top_row_of_app_1_tabs():
    return html.Div(
        children=[
            dcc.Tabs(
                id="dash-tabs",
                value='tab-1',
                children=[
                    dcc.Tab(label='Tab 1', value='tab-1', style=tab_on_row_1_style,
                            selected_style=tab_on_row_1_selected_style),
                    dcc.Tab(label='Tab 2', value='tab-2', style=tab_on_row_1_style,
                            selected_style=tab_on_row_1_selected_style),
                    dcc.Tab(label='Tab 3', value='tab-3', style=tab_on_row_1_style,
                            selected_style=tab_on_row_1_selected_style),
                    dcc.Tab(label='Tab 4', value='tab-4', style=tab_on_row_1_style,
                            selected_style=tab_on_row_1_selected_style),
                ],
                style=tabs_row_1_style
            ),
            html.Div(id='dash-tabs-container')
        ],
    )


def plotly_sample_app():
    return html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='xaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value='Fertility rate, total (births per woman)'
                ),
                dcc.RadioItems(
                    id='xaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                    value='Linear',
                    labelStyle={'display': 'inline-block'}
                )
            ], style={'width': '48%', 'display': 'inline-block'}),

            html.Div([
                dcc.Dropdown(
                    id='yaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value='Life expectancy at birth, total (years)'
                ),
                dcc.RadioItems(
                    id='yaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                    value='Linear',
                    labelStyle={'display': 'inline-block'}
                )
            ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
        ]),

        dcc.Graph(id='indicator-graphic'),

        dcc.Slider(
            id='year--slider',
            min=df['Year'].min(),
            max=df['Year'].max(),
            value=df['Year'].max(),
            marks={str(year): str(year) for year in df['Year'].unique()},
            step=None
        )
    ])


layout = html.Div(
    id='app_1_page_layout',
    children=[
        top_row_of_app_1_tabs(),
        plotly_sample_app(),
    ])
