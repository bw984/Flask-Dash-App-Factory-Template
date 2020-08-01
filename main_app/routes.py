from flask import Blueprint, render_template, redirect

server_bp = Blueprint('main', __name__)


@server_bp.route('/')
def index():
    user = {'username': 'User'}
    return render_template("index.html", title='Home Page', user=user)


@server_bp.route('/non_dash_app')
def non_dash_page():
    user = {'username': 'Some Unrelated Non Dash App or Page'}
    return render_template("index.html", title='Non Dash Page', user=user)


@server_bp.route('/app_1/')
def app_1_template():
    return render_template('dash.html', dash_url='/app_1_raw_dash/')


@server_bp.route('/app_2/')
def app_2_template():
    return render_template('dash.html', dash_url='/app_2_raw_dash/')



