#!/usr/bin/env python3
"""
    Purpose:
        App File and Entry Point for Flask API

    function call:
        export FLASK_APP=app.py; python3 -m flask run
"""

# Python Library Imports
import sys
import os
import logging
import json
from flask import Flask, Response,\
    request, session, g,\
    redirect, url_for, abort,\
    render_template, flash

# Custom Python Library Imports
current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, current_path + '/../')
from config import config
from classes.trello import Trello

# Import config and logging details
CONFIGS = config.Config.get()
logging = CONFIGS.get_logging()

# Start Flask App
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """

    """
    logging.info('Request Called: {request}'.format(request=request))

    content = open('../README.md')
    return Response(content, mimetype='ext/markdown; charset=UTF-8')


@app.route('/boards', methods=['GET'])
def get_boards():
    """

    """

    trello_object = Trello()
    available_boards = trello_object.get_boards()

    return_payload = {
        'data': {
            'available_boards': available_boards
        }
    }

    return Response(
        json.dumps(return_payload), 
        mimetype='application/json; charset=UTF-8'
    )


@app.route('/board/<board_id>', methods=['GET'])
def get_board_details(board_id):
    """

    """

    return_payload = {}

    return Response(
        json.dumps(return_payload), 
        mimetype='application/json; charset=UTF-8'
    )


@app.route('/lists/<board_id>', methods=['GET'])
def get_lists(board_id):
    """

    """

    return_payload = {}

    return Response(
        json.dumps(return_payload), 
        mimetype='application/json; charset=UTF-8'
    )


@app.route('/list/<list_id>', methods=['GET'])
def get_list_details(list_id):
    """

    """

    return_payload = {}

    return Response(
        json.dumps(return_payload), 
        mimetype='application/json; charset=UTF-8'
    )


@app.route('/cards/<list_id>', methods=['GET'])
def get_cards(list_id):
    """

    """

    return_payload = {}

    return Response(
        json.dumps(return_payload), 
        mimetype='application/json; charset=UTF-8'
    )


@app.route('/card/<card_id>', methods=['GET'])
def get_card_details(card_id):
    """

    """

    return_payload = {}

    return Response(
        json.dumps(return_payload), 
        mimetype='application/json; charset=UTF-8'
    )
