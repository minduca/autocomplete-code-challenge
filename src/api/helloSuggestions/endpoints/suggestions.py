# Choice of framework
    # I was between Flask and Django, since both are well stablished web
    # frameworks for python.  I decided to stick with Flask because from what
    # I saw Django uses a "batteries included" approach that brings the gorilla
    # and whole forest when all you asked for was a banana.  Flask on the other
    # hand is is this web microframework that contains only the core tools for
    # web development, which seems a better fit for a simple scenario such
    # as this.
from helloSuggestions import searchEngine, serviceHost
from helloSuggestions.place import Place
from helloSuggestions.serialisationHelper import toJson
from typing import Tuple
from flask import request
from flask_restplus import Resource

@serviceHost.api.route('/suggestions')
class SuggestionsApi(Resource):

    def get(self):
        query = request.args.get('q')
        places : Tuple[Place] = searchEngine.search(query)
        return toJson(places)
