#!/usr/bin/python3
"""A flask app to serve REST api service
this is the main application that calls a registered blueprint
"""

from .views import app_views
from flask import Flask, make_response, jsonify
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(exception):
    """action to take when the app is being closed or exited
    """
    storage.close()


@app.errorhandler(404)
def not_found_err(error):
    """custom 404 error in JSON format instead of HTML
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    if not os.getenv('HBNB_API_HOST'):
        host = '0.0.0.0'
    else:
        host = os.getenv('HBNB_API_HOST')
    if not os.getenv('HBNB_API_PORT'):
        port = 5000
    else:
        port = os.getenv('HBNB_API_PORT')

    app.run(host=host, port=port, threaded=True)
