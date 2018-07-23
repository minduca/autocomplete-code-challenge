# Choice of framework
# I was between Flask and Django, since both are well stablished web
# frameworks for python.  I decided to stick with Flask because from what
# I saw Django uses a "batteries included" approach that brings the gorilla
# and whole forest when all you asked for was a banana.  Flask on the other
# hand is is this web microframework that contains only the core tools for
# web development, which seems a better fit for a simple scenario such
# as this.
from typing import Tuple
from decimal import Decimal
from flask import request
from flask_restplus import Resource
from hello import searchEngine, host
from hello.search.placeSearchResult import PlaceSearchResult
from hello.endpoints.models import PlaceDto, PlaceDtoMapper, suggestionsDtoDescription


@host.api.route('/suggestions')
class SuggestionsApi(Resource):

    @host.api.marshal_with(suggestionsDtoDescription)
    def get(self) -> dict:

        query: str = request.args.get('q')
        latitude: Decimal = None
        longitude: Decimal = None

        try:
            latitudeStr: str = request.args.get('latitude')
            longitudeStr: str = request.args.get('longitude')

            if latitudeStr and longitudeStr:
                latitude = Decimal(latitudeStr)
                longitude = Decimal(longitudeStr)
        except ValueError:
            pass

        result: PlaceSearchResult = searchEngine.search(query, latitude, longitude)

        mapper = PlaceDtoMapper()
        placesDto: Tuple[PlaceDto, ...] = tuple(map(mapper.toDto, result.places))

        return {'suggestions': placesDto}
