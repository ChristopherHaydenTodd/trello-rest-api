"""
    Purpose: 
        Trello Class for wrapping API and performing actions
        on boards/cards/lists

"""

# Python Library Imports
import sys
import os
import trello
import logging

# Custom Python Library Imports
current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, current_path + '/../')
from config import config

# Import config details
CONFIGS = config.Config.get()


class Trello(object):
    """
        Base Trello Class
    """

    def __init__(self):
        """
            Initilize the Base CMTS Class.
            Class Properties Should be set in Child Class
        Args:
            fqdn (string): hostname or fqdn
        """

        logging.info('Creating Trello Object and Instantiating API')
        logging.info(CONFIGS.TRELLO_APP_KEY)
        logging.info(CONFIGS.TRELLO_APP_TOKEN)

        self.trello_api =\
            trello.TrelloApi(apikey=CONFIGS.TRELLO_APP_KEY)
        self.trello_api.set_token(CONFIGS.TRELLO_APP_TOKEN)

        self.known_boards = {
            'To Do List': '56e1cbce8bde063d47d1db02',
        }

        self.board = None
        self.lists = None
        self.cards = None


    def get_boards(self):
        """
        Purpose:
            Return Known Boards
        Args:
            N/A
        Return
            boards (list of string): List of available boards
                to select from

        Note: Need ID from Trello to pull board details, 
        can't let this be dynamic until I figure out a way
        to get all boards available to a user
        """

        return list(self.known_boards.keys())

    # def get_board(board_name):
    #     """
    #         Get the Board Object from the Trello API
    #         Based on Passed in Boards
    #     """

    # def get_lists(self, board_id):
    #     """
    #         Initilize the Base CMTS Class.
    #         Class Properties Should be set in Child Class
    #     Args:
    #         fqdn (string): hostname or fqdn
    #     """

    #     return

    # def get_lists(self, list_id):
    #     """
    #         Initilize the Base CMTS Class.
    #         Class Properties Should be set in Child Class
    #     Args:
    #         fqdn (string): hostname or fqdn
    #     """

        return