"""
This file is the entry point of the application, equivalent to the main() method pattern on many programming languages
"""

# Disclaimer : I am not literate in python.  I didn't have any previous
    # background in this language prior to this small application.  Even its
    # famous libraries were relativelly unknown to me.  But altough it's the
    # first time I write in python, I do take responsability for the design
    # choices I made with the languages capabilities that I discovered whlist
    # building this simple app.

# Choice of framework
    # I was between Flask and Django, since both are well stablished web
    # frameworks for python.  I decided to stick with Flask because from what
    # I saw Django uses a "batteries included" approach that brings the gorilla
    # and whole forest when all you asked for was a banana.  Flask on the other
    # hand is is this web microframework that contains only the core tools for
    # web development, which seems a better fit for a simple scenario such
    # as this.

from flask import Flask
from .placeSearchEngine import PlaceSearchEngine
from .placeSearchConfig import PlaceSearchConfig
from .placeSearchStrategy import VeryDummyPlaceSearchStrategy
from .db import InMemoryDb

# In a more complex scenatio we could use a builder instead of a factory to
# create more elaborate instances
def createSearchEngine() -> PlaceSearchEngine:
    config = PlaceSearchConfig(maxNumberResults=10) #raw type arguments explicity declared for readability purposes
    db = InMemoryDb()
    strategy = VeryDummyPlaceSearchStrategy(db)
    return PlaceSearchEngine(strategy, config)

app = Flask(__name__) #application factory
searchEngine = createSearchEngine() #in a local method to avoid spread and restraint scope of intermediate
                                    #variables.
import helloSuggestions.api