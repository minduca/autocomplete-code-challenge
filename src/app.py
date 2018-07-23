# Start the application

import asyncio
from flask import Flask
from flask_restplus import Api, Resource

from hello import settings
from hello.search.placeSearchEngine import PlaceSearchEngine
from hello.search.placeSearchQueryStrategy import LevenshteinTrieSearchQueryStrategy
from hello.tsvPlacesReader import TsvPlacesReader
from hello.core import IDb
from hello.inMemoryDb import InMemoryDb
from hello.endpoints.models import SuggestionsDescriptor
from hello.endpoints.suggestions import SuggestionsApi

app = Flask(__name__)
api = Api(app, version="1.0", title="Code challenge - Suggestions API")
searchEngine: PlaceSearchEngine = None


@api.route('/suggestions')
class SuggestionsApiDescriptor(Resource):
    @api.marshal_with(SuggestionsDescriptor().createDescription(api))
    def get(self) -> dict:
        return SuggestionsApi(searchEngine).autocomplete()


class InfraFactory:

    async def createSeach(self) -> PlaceSearchEngine:

        # create the database
        db: IDb = await self._createDb()

        # create the search engine
        return await self._createSearchEngine(db)

    async def _createSearchEngine(self, db: IDb) -> PlaceSearchEngine:
        strategy = LevenshteinTrieSearchQueryStrategy(db, settings.SCORE_WEIGHT_QUERY_SEARCH)
        await strategy.initAsync()

        return PlaceSearchEngine(strategy,
                                 maxNumberResults=settings.MAX_NUMBER_RESULTS,
                                 scoreWeightPopulationSize=settings.SCORE_WEIGHT_POPULATION_SIZE,
                                 scoreWeightCoordinatesDistance=settings.SCORE_WEIGHT_COORDINATES_DISTANCE)

    async def _createDb(self) -> IDb:
        dataReader = TsvPlacesReader(settings.DATA_SOURCE_PATH)
        db: IDb = InMemoryDb(dataReader)
        await db.initAsync()
        return db


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    task = loop.create_task(InfraFactory().createSeach())
    loop.run_until_complete(task)
    searchEngine = task.result()
    app.run()
