from flask import Flask
from flask.helpers import get_root_path
from dash import Dash


def create_app():
    server = Flask(__name__)
    # configure flask app/server here

    # register all dash apps
    from main_app.app_2.layout import layout as app_2_layout
    from main_app.app_2.callbacks import register_callbacks as app_2_callbacks
    register_dash_app(server, 'App 1', 'app_2_raw_dash', app_2_layout, app_2_callbacks)

    from main_app.app_1.layout import layout as app_1_layout
    from main_app.app_1.callbacks import register_callbacks as app_1_callbacks
    register_dash_app(server, 'App 2', 'app_1_raw_dash', app_1_layout, app_1_callbacks)

    # register extensions here
    register_blueprints(server)

    return server


def register_dash_app(flask_server, title, base_pathname, layout, register_callbacks_func):
    # Meta tags for viewport responsiveness
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    my_dash_app = Dash(__name__,
                       server=flask_server,
                       url_base_pathname=f'/{base_pathname}/',
                       assets_folder=get_root_path(__name__) + f'/{base_pathname}/assets/',
                       meta_tags=[meta_viewport])

    with flask_server.app_context():
        my_dash_app.title = title
        my_dash_app.layout = layout
        register_callbacks_func(my_dash_app)


def register_blueprints(server):
    from main_app.routes import server_bp
    server.register_blueprint(server_bp)
