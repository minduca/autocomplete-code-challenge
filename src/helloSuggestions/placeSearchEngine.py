from .place import Place
from .core import IPlaceSearchStrategy
from .placeSearchConfig import PlaceSearchConfig
from typing import Tuple

class PlaceSearchEngine(object):
    
    def __init__(self, searchStrategy: IPlaceSearchStrategy, config: PlaceSearchConfig):
        self.searchStrategy = searchStrategy
        self.config = config

    def search(self, query) -> Tuple[Place]:

        reponse: Tuple[Place] = ()

        if self.config.maxNumberResults < 0: raise ValueError("value must be superior to 0")

        queryParsed = None

        if query:
            # lower() since apparently there is no case insensitive comparison in python
            # For simplicity purposes, we gonna deliberately scape case match for the recommendation.
            queryParsed: str = query.strip().lower()

        if queryParsed:
            reponse = self.searchStrategy.search(query)
            reponse = reponse[0:self.config.maxNumberResults] # split the array (it won't allocate extra space when results are lower than the maximum allowed)

        return reponse


