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
from hello.endpoints.models import PlaceDescriptionFactory
from hello.endpoints.suggestions import SuggestionsApi

app = Flask(__name__)
api = Api(app, version="1.0", title="Code challenge - Suggestions API")
searchEngine: PlaceSearchEngine = None
descriptionFactory = PlaceDescriptionFactory()


@api.route('/suggestions')
class SuggestionsApiDescription(Resource):

    @api.marshal_with(descriptionFactory.createSuggestionsDtoDescription(api))
    def get(self) -> dict:
        return SuggestionsApi(searchEngine).autocomplete()


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


async def run():

    infra = InfraFactory()

    # create the database
    db: IDb = await infra.createDb()

    # create the search engine
    global searchEngine
    searchEngine = await infra.createSearchEngine(db)

    app.run(use_reloader=True)

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    task = loop.create_task(run())
    loop.run_until_complete(task)
