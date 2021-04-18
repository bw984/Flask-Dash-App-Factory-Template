from flask import Flask
from flask.helpers import get_root_path
from dash import Dash
from os import getpid


def create_app(dash_debug, dash_auto_reload):
    server = Flask(__name__, static_folder='static')

    # configure flask app/server here
    server.config.from_object('config.Config')

    # register all dash apps
    from main_app.app_1.layout import layout as app_1_layout
    from main_app.app_1.callbacks import register_callbacks as app_1_callbacks
    register_dash_app(
        flask_server=server,
        title='App 1',
        base_pathname='app_1_raw_dash',
        layout=app_1_layout,
        register_callbacks_funcs=[app_1_callbacks],
        dash_debug=dash_debug,
        dash_auto_reload=dash_auto_reload
    )

    from main_app.app_2.layout import layout as app_2_layout
    from main_app.app_2.callbacks import register_callbacks as app_2_callbacks
    register_dash_app(
        flask_server=server,
        title='App 2',
        base_pathname='app_2_raw_dash',
        layout=app_2_layout,
        register_callbacks_funcs=[app_2_callbacks],
        dash_debug=dash_debug,
        dash_auto_reload=dash_auto_reload
    )

    # register extensions here
    register_blueprints(server)

    # if running on gunicorn with multiple workers this message should print once for each worker if preload_app is set to False
    print(f'Flask With Dash Apps Built Successfully with PID {str(getpid())}.')
    return server


def register_dash_app(flask_server, title, base_pathname, layout, register_callbacks_funcs, dash_debug, dash_auto_reload):
    # Meta tags for viewport responsiveness
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    my_dash_app = Dash(
        __name__,
        server=flask_server,
        url_base_pathname=f'/{base_pathname}/',
        assets_folder=get_root_path(__name__) + '/static/',
        meta_tags=[meta_viewport],
        # external_stylesheets=[],
        # external_scripts=[]
    )

    with flask_server.app_context():
        my_dash_app.title = title
        my_dash_app.layout = layout
        my_dash_app.css.config.serve_locally = True
        my_dash_app.enable_dev_tools(debug=dash_debug, dev_tools_hot_reload=dash_auto_reload)
        for call_back_func in register_callbacks_funcs:
            call_back_func(my_dash_app)


def register_blueprints(server):
    from main_app.routes import server_bp
    server.register_blueprint(server_bp)
