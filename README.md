# Trello Rest API

The Trello Rest API project was created to integrate with trello and automate
actions taken in the UI.

## Table of Contents

- [Dependencies](#dependencies)
- [App](#app)
- [Classes](#classes)

## Dependencies

### Python Packages

- os
- sys
- wrapt
- logging
- argparse (ArgumentParser)
- datetime (datetime)
- pandas (pd)
- flask
- json
- trello

## App

Holds Flask files for starting server-side API and handling requests

### [app.py](https://github.com/ChristopherHaydenTodd/trello-rest-api/blob/master/app/app.py)

App File and Entry Point for Flask API

Usage:
```sh
export FLASK_APP=app.py; python3 -m flask run
```

## Classes

Holds Trello Class for interfacing with the Trello API

### [trello.py](https://github.com/ChristopherHaydenTodd/trello-rest-api/blob/master/classes/trello.py)

Trello Class for wrapping API and performing actions
on boards/cards/lists

Usage:
```python
from classes.trello import Trello
trello_object = Trello()
available_boards = trello_object.get_boards()
```

## Example API Calls

### Get all Boards
http://localhost:5000/boards

### Get "To Do List" Board Details
http://localhost:5000/board/56e1cbce8bde063d47d1db02

### Get Lists on "To Do List" Board
http://localhost:5000/lists/56e1cbce8bde063d47d1db02

### Get List "To Do" on "To Do List" Board
http://localhost:5000/list/56e1cbd6f83f7f95f11d7ca7

### Get Cards on "To Do" List on "To Do List" Board
http://localhost:5000/cards/56e1cbd6f83f7f95f11d7ca7

### Get Card "Fix Basement Roof" on List "To Do" on "To Do" Board
http://localhost:5000/card/56e22c4b6f7f6f5967b002b2%