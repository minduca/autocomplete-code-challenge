from helloSuggestions.search.placeSearchEngine import PlaceSearchEngine
from helloSuggestions.search.placeSearchConfig import PlaceSearchConfig
from helloSuggestions.search.placeSearchStrategy import VeryDummyPlaceSearchStrategy
from helloSuggestions.db import InMemoryDb

def createSearchEngine(maxNumberResults: int) -> PlaceSearchEngine:
    config = PlaceSearchConfig(maxNumberResults)
    db = InMemoryDb()
    strategy = VeryDummyPlaceSearchStrategy(db)
    return PlaceSearchEngine(strategy, config)