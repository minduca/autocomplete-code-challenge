"""
Entry point of the application
"""

from helloSuggestions.search.placeSearchEngineFactory import createSearchEngine
from helloSuggestions.endpoints.endpointshost import EndpointsHost
from helloSuggestions import settings

# create the search engine
searchEngine = createSearchEngine(settings.MAX_NUMBER_RESULTS)

# create the service host
serviceHost = EndpointsHost()

def run(serverHost: str, port: int):
    serviceHost.run(serverHost, port)