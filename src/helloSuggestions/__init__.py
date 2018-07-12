"""
Entry point of the application
"""
import asyncio
from helloSuggestions import settings
from helloSuggestions.endpoints.endpointshost import EndpointsHost
from helloSuggestions.search.placeSearchEngine import PlaceSearchEngine
from helloSuggestions.search.placeSearchConfig import PlaceSearchConfig
from helloSuggestions.search.placeSearchStrategy import VeryDummyPlaceSearchStrategy
from helloSuggestions.tsvPlacesReader import TsvPlacesReader
from helloSuggestions.core import IDb, Tuple, Place, IDataReader
from helloSuggestions.inMemoryDb import InMemoryDb

searchEngine : PlaceSearchEngine = None
host : EndpointsHost = None

async def run(serverHost: str, port: int):
    
    infra = InfraFactory()

    #create the database
    db : IDb = await infra.createDb()

    # create the search engine
    global searchEngine 
    searchEngine = infra.createSearchEngine(db)
    
    # create and starts the service host
    global host
    host = EndpointsHost()
    host.run(serverHost, port)

#Infrastructure initialization.
class InfraFactory(object):

    def createSearchEngine(self, db : IDb) -> PlaceSearchEngine:
        config = PlaceSearchConfig(settings.MAX_NUMBER_RESULTS)
        strategy = VeryDummyPlaceSearchStrategy(db)
        return PlaceSearchEngine(strategy, config)

    async def createDb(self) -> IDb:
        dataReader = TsvPlacesReader(settings.DATA_SOURCE_PATH)
        db : IDb = InMemoryDb(dataReader)
        await db.loadAsync()
        return db

