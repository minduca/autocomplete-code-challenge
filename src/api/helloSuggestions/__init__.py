"""
This file is the entry point of the application, equivalent to the main() method pattern on many programming languages
"""

# Disclaimer : I am not literate in python.  I didn't have any previous
    # background in this language prior to this small application.  Even its
    # famous libraries were relativelly unknown to me.  But altough it's the
    # first time I write in python, I do take responsability for the design
    # choices I made with the languages capabilities that I discovered whlist
    # building this simple app.

from flask import Flask
from helloSuggestions.search.placeSearchEngineFactory import createSearchEngine
from helloSuggestions import settings

app = Flask(__name__)

# create the search engine
searchEngine = createSearchEngine(settings.MAX_NUMBER_RESULTS)

# init suggestions api
import helloSuggestions.suggestionsApi