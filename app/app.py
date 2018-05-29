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
    Purpose:
        Return All Boards Available to Pull
    Args:
        N/A
    """

    trello_object = Trello()
    available_boards =\
        trello_object.get_boards()

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
    Purpose:
        Return All Board Details Based on Board Id
    Args:
        board_id (string)
    """

    trello_object = Trello()
    board_details =\
        trello_object.get_board_details(board_id)

    return_payload = {
        'data': {
            'board_details': board_details
        }
    }

    return Response(
        json.dumps(return_payload), 
        mimetype='application/json; charset=UTF-8'
    )


@app.route('/lists/<board_id>', methods=['GET'])
def get_lists(board_id):
    """
    Purpose:
        Return All Lists Based on Board
    Args:
        board_id (string)
    """

    trello_object = Trello()
    lists =\
        trello_object.get_lists(board_id)

    return_payload = {
        'data': {
            'lists': lists
        }
    }

    return Response(
        json.dumps(return_payload), 
        mimetype='application/json; charset=UTF-8'
    )


@app.route('/list/<list_id>', methods=['GET'])
def get_list_details(list_id):
    """
    Purpose:
        Return All List Details Based on List Id
    Args:
        list_id (string)
    """

    trello_object = Trello()
    list_details =\
        trello_object.get_list_details(list_id)

    return_payload = {
        'data': {
            'list_details': list_details
        }
    }

    return Response(
        json.dumps(return_payload), 
        mimetype='application/json; charset=UTF-8'
    )


@app.route('/cards/<list_id>', methods=['GET'])
def get_cards(list_id):
    """
    Purpose:
        Return All Cards Based on List ID
    Args:
        list_id (string)
    """

    trello_object = Trello()
    cards =\
        trello_object.get_cards(
            board_id=None, list_id=list_id)

    return_payload = {
        'data': {
            'cards': cards
        }
    }

    return Response(
        json.dumps(return_payload), 
        mimetype='application/json; charset=UTF-8'
    )


@app.route('/card/<card_id>', methods=['GET'])
def get_card_details(card_id):
    """
    Purpose:
        Return All Card Details Based on Card Id
    Args:
        card_id (string)
    """

    trello_object = Trello()
    card_details =\
        trello_object.get_card_details(card_id)

    return_payload = {
        'data': {
            'card_details': card_details
        }
    }

    return Response(
        json.dumps(return_payload), 
        mimetype='application/json; charset=UTF-8'
    )


@app.route('/test', methods=['GET'])
def test_endpoint():
    """

    """

    trello_object = Trello()

    import pdb; pdb.set_trace()

    return_payload = {}

    return Response(
        json.dumps(return_payload), 
        mimetype='application/json; charset=UTF-8'
    )
