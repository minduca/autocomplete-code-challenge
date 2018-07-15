from hello.core import IPlaceSearchQueryStrategy, Place, PlaceScore, Tuple
from hello.search.placeSearchResult import PlaceSearchResult
from hello.search.placeSearchConfig import PlaceSearchConfig
import time

class PlaceSearchEngine(object):
    
    def __init__(self, searchStrategy: IPlaceSearchQueryStrategy, config: PlaceSearchConfig):
        self._searchStrategy : IPlaceSearchQueryStrategy = searchStrategy
        self._config : PlaceSearchConfig = config

    def search(self, query) -> PlaceSearchResult:

        places : Tuple[PlaceScore, ...] = ()

        if self._config.maxNumberResults <= 0: raise ValueError("value must be superior to 0")

        queryParsed : str = None

        if query:
            queryParsed : str = query.strip()

        if queryParsed:

            start = time.time()
            places = self._searchStrategy.search(queryParsed)
            end = time.time()
            places = places[0:self._config.maxNumberResults]

        return PlaceSearchResult(places, start, end)



