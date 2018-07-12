"""
Entry point of the application
"""

from helloSuggestions import settings
from helloSuggestions.endpoints.endpointshost import EndpointsHost
from helloSuggestions.search.placeSearchEngine import PlaceSearchEngine
from helloSuggestions.search.placeSearchConfig import PlaceSearchConfig
from helloSuggestions.search.placeSearchStrategy import VeryDummyPlaceSearchStrategy
from helloSuggestions.tsvPlacesReader import TsvPlacesReader
from helloSuggestions.core import IDb, Tuple, Place, IDataReader
from helloSuggestions.inMemoryDb import InMemoryDb

searchEngine : PlaceSearchEngine = None
serviceHost : EndpointsHost = None

def run(serverHost: str, port: int):
    
    infra = InfraFactory()

    #create the database
    db : IDb = infra.createDb()

    # create the search engine
    global searchEngine 
    searchEngine = infra.createSearchEngine(db)
    
    # create and starts the service host
    global serviceHost
    serviceHost = EndpointsHost()
    serviceHost.run(serverHost, port)

#Infrastructure initialization.
class InfraFactory(object):

    def createSearchEngine(self, db : IDb) -> PlaceSearchEngine:
        config = PlaceSearchConfig(settings.MAX_NUMBER_RESULTS)
        strategy = VeryDummyPlaceSearchStrategy(db)
        return PlaceSearchEngine(strategy, config)

    def createDb(self) -> IDb:
        dataReader = TsvPlacesReader(settings.DATA_SOURCE_PATH)
        db : IDb = InMemoryDb(dataReader)
        db.loadAsync()
        return db

