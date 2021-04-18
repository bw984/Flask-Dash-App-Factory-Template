"""Application entry point."""
from main_app import create_app
dash_debug = False
flask_debug = False

server = create_app(dash_debug)

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=8000, debug=flask_debug, threaded=False)
