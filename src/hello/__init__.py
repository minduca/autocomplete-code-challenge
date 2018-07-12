# Entry point of the application

import asyncio
from hello import settings
from hello.endpoints.endpointshost import EndpointsHost
from hello.search.placeSearchEngine import PlaceSearchEngine
from hello.search.placeSearchConfig import PlaceSearchConfig
from hello.search.placeSearchStrategy import VeryDummyPlaceSearchStrategy
from hello.tsvPlacesReader import TsvPlacesReader
from hello.core import IDb, Tuple, Place, IDataReader
from hello.inMemoryDb import InMemoryDb

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

