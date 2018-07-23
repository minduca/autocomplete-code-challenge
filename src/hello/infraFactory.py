import asyncio

from hello import settings
from hello.search.placeSearchEngine import PlaceSearchEngine
from hello.search.placeSearchQueryStrategy import LevenshteinTrieSearchQueryStrategy
from hello.tsvPlacesReader import TsvPlacesReader
from hello.core import IDb
from hello.inMemoryDb import InMemoryDb


class InfraFactory:

    def createSeach(self) -> PlaceSearchEngine:

        # I'm intentionnaly disabling the async operation
        # to investigate later a very specific problem
        # that occurs when the app is deployed to heroku
        loop = asyncio.get_event_loop()
        task = loop.create_task(self._createSearchAsync())
        loop.run_until_complete(task)
        return task.result()

    async def _createSearchAsync(self) -> PlaceSearchEngine:
        # create the database
        db: IDb = await self._loadDbAsync()

        # create the search engine
        return await self._loadSearchEngineAsync(db)

    async def _loadSearchEngineAsync(self, db: IDb) -> PlaceSearchEngine:
        strategy = LevenshteinTrieSearchQueryStrategy(db, settings.SCORE_WEIGHT_QUERY_SEARCH)
        await strategy.initAsync()

        return PlaceSearchEngine(strategy,
                                 maxNumberResults=settings.MAX_NUMBER_RESULTS,
                                 scoreWeightPopulationSize=settings.SCORE_WEIGHT_POPULATION_SIZE,
                                 scoreWeightCoordinatesDistance=settings.SCORE_WEIGHT_COORDINATES_DISTANCE)

    async def _loadDbAsync(self) -> IDb:
        dataReader = TsvPlacesReader(settings.DATA_SOURCE_PATH)
        db: IDb = InMemoryDb(dataReader)
        await db.initAsync()
        return db
