from helloSuggestions.core import IPlaceSearchStrategy, Tuple, Place
from helloSuggestions.search.placeSearchConfig import PlaceSearchConfig

class PlaceSearchEngine(object):
    
    def __init__(self, searchStrategy: IPlaceSearchStrategy, config: PlaceSearchConfig):
        self._searchStrategy : IPlaceSearchStrategy = searchStrategy
        self._config : PlaceSearchConfig = config

    def search(self, query) -> Tuple[Place, ...]:

        reponse : Tuple[Place, ...] = ()

        if self._config.maxNumberResults <= 0: raise ValueError("value must be superior to 0")

        queryParsed = None

        if query:
            # lower() since apparently there is no case insensitive comparison
            # in python
            # For simplicity purposes, we gonna deliberately scape case match
            # for the recommendation.
            queryParsed : str = query.strip().lower()

        if queryParsed:
            reponse = self._searchStrategy.search(queryParsed)
            reponse = reponse[0:self._config.maxNumberResults] # split the array (it won't allocate extra space when results are lower than
                                                              # the maximum allowed)

        return reponse


