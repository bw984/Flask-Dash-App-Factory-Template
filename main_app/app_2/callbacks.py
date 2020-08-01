from dash.dependencies import Input, Output


def register_callbacks(dash_app):
    @dash_app.callback(
        Output(component_id='my-output', component_property='children'),
        [Input(component_id='my-input', component_property='value')]
    )
    def update_output_div(input_value):
        return 'Output: {}'.format(input_value)
