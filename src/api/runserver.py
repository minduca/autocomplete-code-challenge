"""
This script runs the helloSuggestions application using a development server.
"""

from os import environ
from helloSuggestions import app

if __name__ == '__main__':
    app.run()
