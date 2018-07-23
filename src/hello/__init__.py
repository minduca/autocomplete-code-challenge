# Entry point of the application

import asyncio
from hello import settings
from hello.endpoints.endpointshost import EndpointsHost
from hello.search.placeSearchEngine import PlaceSearchEngine
from hello.search.placeSearchQueryStrategy import LevenshteinTrieSearchQueryStrategy
from hello.tsvPlacesReader import TsvPlacesReader
from hello.core import IDb, Place, IDataReader
from hello.inMemoryDb import InMemoryDb

searchEngine: PlaceSearchEngine = None
host: EndpointsHost = None


async def run(serverHost: str, port: int):

    infra = InfraFactory()

    # create the database
    db: IDb = await infra.createDb()

    # create the search engine
    global searchEngine
    searchEngine = await infra.createSearchEngine(db)

    # create and starts the service host
    global host
    host = EndpointsHost()
    host.run(serverHost, port)

# Infrastructure initialization.


class InfraFactory:

    async def createSearchEngine(self, db: IDb) -> PlaceSearchEngine:
        strategy = LevenshteinTrieSearchQueryStrategy(db, settings.SCORE_WEIGHT_QUERY_SEARCH)
        await strategy.initAsync()

        return PlaceSearchEngine(strategy,
                                 maxNumberResults=settings.MAX_NUMBER_RESULTS,
                                 scoreWeightPopulationSize=settings.SCORE_WEIGHT_POPULATION_SIZE,
                                 scoreWeightCoordinatesDistance=settings.SCORE_WEIGHT_COORDINATES_DISTANCE)

    async def createDb(self) -> IDb:
        dataReader = TsvPlacesReader(settings.DATA_SOURCE_PATH)
        db: IDb = InMemoryDb(dataReader)
        await db.initAsync()
        return db
