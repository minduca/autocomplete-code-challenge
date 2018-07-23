# Start the application

from flask import Flask
from flask_restplus import Api, Resource
from hello.endpoints.models import SuggestionsDescriptor
from hello.endpoints.suggestions import SuggestionsApi
from hello.search.placeSearchEngine import PlaceSearchEngine
from hello.infraFactory import InfraFactory

app = Flask(__name__)
api = Api(app, version="1.0", title="Code challenge - Suggestions API")
searchEngine: PlaceSearchEngine = InfraFactory().createSeach()


@api.route('/suggestions')
class SuggestionsApiDescriptor(Resource):
    @api.marshal_with(SuggestionsDescriptor().createDescription(api))
    def get(self) -> dict:
        return SuggestionsApi(searchEngine).autocomplete()


if __name__ == '__main__':
    app.run()
