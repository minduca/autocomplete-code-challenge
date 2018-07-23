from typing import Tuple
from decimal import Decimal
from flask import request
from hello.search.placeSearchEngine import PlaceSearchEngine
from hello.search.placeSearchResult import PlaceSearchResult
from hello.endpoints.models import PlaceDto, PlaceDtoMapper


class SuggestionsApi:

    def __init__(self, searchEngine: PlaceSearchEngine):
        self._searchEngine = searchEngine

    def autocomplete(self) -> dict:

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

        result: PlaceSearchResult = self._searchEngine.search(query, latitude, longitude)

        mapper = PlaceDtoMapper()
        placesDto: Tuple[PlaceDto, ...] = tuple(map(mapper.toDto, result.places))

        return {'suggestions': placesDto}
