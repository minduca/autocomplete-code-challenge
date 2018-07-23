import time
from decimal import Decimal
from typing import List
from autocomplete.resultHandlers import IResultHandler, ZeroToOneScaleScoreAggregator, CompositeHandlers
from hello.core import IPlaceSearchQueryStrategy, ResultMatch
from .placeSearchResult import PlaceSearchResult
from .resultHandlers import RedundantPlacesIdFilter, PlaceDisplayNameMatchOverride, PopulationSizeScoreWeightsGenerator, CoordinatesScoreWeightsGenerator

# Manages the whole flow of the search


class PlaceSearchEngine:

    def __init__(self,
                 searchStrategy: IPlaceSearchQueryStrategy,
                 maxNumberResults: int,
                 scoreWeightPopulationSize: int,
                 scoreWeightCoordinatesDistance: int):

        if maxNumberResults <= 0:
            raise ValueError("The number of results to be returned must be superior to zero")

        self._searchStrategy: IPlaceSearchQueryStrategy = searchStrategy
        self._maxNumberResults: int = maxNumberResults
        self._scoreWeightPopulationSize = scoreWeightPopulationSize
        self._scoreWeightCoordinatesDistance = scoreWeightCoordinatesDistance

    def search(self, query: str, latitude: Decimal = None, longitude: Decimal = None) -> PlaceSearchResult:

        places: List[ResultMatch] = []

        queryParsed: str = None

        if query:
            queryParsed: str = query.strip()

        start = time.time()

        if queryParsed:
            resultHandler: IResultHandler = self._buildResultHandler(latitude, longitude)
            places = self._searchStrategy.search(queryParsed, resultHandler)
            places = list(filter(lambda r: r.getScore() > 0, places))[0:self._maxNumberResults]

        end = time.time()

        return PlaceSearchResult(tuple(places), start, end)

    def _buildResultHandler(self, latitude: Decimal, longitude: Decimal) -> IResultHandler:

        resultHandlers: List[IResultHandler] = [
            RedundantPlacesIdFilter(),
            PlaceDisplayNameMatchOverride(),
            PopulationSizeScoreWeightsGenerator(weight=self._scoreWeightPopulationSize)
        ]

        if latitude is not None and longitude is not None:
            resultHandlers.append(CoordinatesScoreWeightsGenerator(latitude, longitude, weight=self._scoreWeightCoordinatesDistance))

        resultHandlers.append(ZeroToOneScaleScoreAggregator())

        return CompositeHandlers(resultHandlers)
