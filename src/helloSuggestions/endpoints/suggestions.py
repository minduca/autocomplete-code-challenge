# Choice of framework
    # I was between Flask and Django, since both are well stablished web
    # frameworks for python.  I decided to stick with Flask because from what
    # I saw Django uses a "batteries included" approach that brings the gorilla
    # and whole forest when all you asked for was a banana.  Flask on the other
    # hand is is this web microframework that contains only the core tools for
    # web development, which seems a better fit for a simple scenario such
    # as this.
from helloSuggestions import searchEngine, host, Tuple
from helloSuggestions.core import PlaceScore
from helloSuggestions.endpoints.models import PlaceDto, PlaceDtoMapper, suggestionsDtoDescription
from flask import request
from flask_restplus import Resource

@host.api.route('/suggestions')
class SuggestionsApi(Resource):

    @host.api.marshal_with(suggestionsDtoDescription)
    def get(self):
        
        query : str = request.args.get('q')
        places : Tuple[PlaceScore, ...] = searchEngine.search(query)
        
        mapper = PlaceDtoMapper()
        placesDto: Tuple[PlaceDto, ...] = tuple(map(mapper.toDto, places))

        return {'suggestions' : placesDto}
