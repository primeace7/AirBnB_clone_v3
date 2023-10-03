#!/usr/bin/python3
"""view page for displaying the status of the api service
"""
from . import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """returns the status of the service when active
    """
    return jsonify({'status': 'OK'})
