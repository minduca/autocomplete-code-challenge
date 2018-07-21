import time
from hello.core import IPlaceSearchQueryStrategy, PlaceScore, Tuple
from .placeSearchResult import PlaceSearchResult
from .placeSearchConfig import PlaceSearchConfig


class PlaceSearchEngine:

    def __init__(self, searchStrategy: IPlaceSearchQueryStrategy, config: PlaceSearchConfig):
        self._searchStrategy: IPlaceSearchQueryStrategy = searchStrategy
        self._config: PlaceSearchConfig = config

    def search(self, query) -> PlaceSearchResult:

        places: Tuple[PlaceScore, ...] = ()

        if self._config.maxNumberResults <= 0:
            raise ValueError("value must be superior to 0")

        queryParsed: str = None

        if query:
            queryParsed: str = query.strip()

        start = time.time()

        if queryParsed:
            places = self._searchStrategy.search(queryParsed)
            places = places[0:self._config.maxNumberResults]

        end = time.time()

        return PlaceSearchResult(places, start, end)
