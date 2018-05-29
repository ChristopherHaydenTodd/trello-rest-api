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
            '56e1cbce8bde063d47d1db02': 'To Do List',
        }

        self.board = None
        self.lists = None
        self.cards = None

    def convert_board_id_to_name(self, board_id):
        """
        Purpose:
            Return Board Name Based on Board ID
        Args:
            board_id (string): Unique ID for Board
        Return
            board_name (string): Non-unique name for board
        """

        return self.known_boards.get(board_id, None)

    def convert_board_name_to_id(self, board_name):
        """
        Purpose:
            Return Board ID Based on Board Name
        Args:
            board_name (string): Non-unique name for board
        Return
            board_id (string): Unique ID for Board
        """

        board_id = None
        for loop_board_id, loop_board_name in\
            self.known_boards.items():
            if board_name == loop_board_name:
                return board_id

        return board_id

    def get_boards(self):
        """
        Purpose:
            Return All Boards Available to Pull
        Args:
            N/A
        Return
            boards (list of string): List of available boards
                to select from

        Note: Need ID from Trello to pull board details, 
        can't let this be dynamic until I figure out a way
        to get all boards available to a user
        """

        return self.known_boards

    def get_board_details(self, board_id):
        """
        Purpose:
            Return All Board Details Based on Board Passed In
        Args:
            board_id (string): Unique ID for Board
        Return
            board_details (dictionary): Board Object from API
        """

        board_details =\
            self.trello_api.boards.get(board_id)
        board_details['cards'] =\
            self.trello_api.boards.get_card(board_id)
        board_details['lists'] =\
            self.trello_api.boards.get_list(board_id)

        return board_details

    def get_lists(self, board_id):
        """
        Purpose:
            Return All Lists in the passed in Board
        Args:
            board_id (string): Unique ID for Board
        Return
            lists (list of string): List of lists boards
                With basic details
        """

        lists = self.trello_api.boards.get_list(board_id)

        return lists

    def get_list_details(self, list_id):
        """
        Purpose:
            Return All List Details Based on List Passed In
        Args:
            list_id (string): Unique ID for List
        Return
            list_details (dictionary): List Object from API
        """

        list_details =\
            self.trello_api.lists.get(list_id)
        list_details['cards'] =\
            self.trello_api.lists.get_card(list_id)

        return list_details

    def get_cards(self, board_id=None, list_id=None):
        """
        Purpose:
            Return All Lists in the passed in Board
        Args:
            board_id (string): Unique ID for Board
        Return
            cards (card of string): List of cards boards
                With basic details
        """

        if board_id:
            cards = self.trello_api.boards.get_card(board_id)
        elif list_id:
            cards = self.trello_api.lists.get_card(list_id)
        else:
            cards = None
        return cards

    def get_card_details(self, card_id):
        """
        Purpose:
            Return All List Details Based on List Passed In
        Args:
            card_id (string): Unique ID for List
        Return
            card_details (dictionary): List Object from API
        """

        card_details =\
            self.trello_api.cards.get(card_id)

        return card_details
