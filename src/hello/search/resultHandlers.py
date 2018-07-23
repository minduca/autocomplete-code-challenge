from decimal import Decimal
from typing import List, Set, Tuple
import geopy.distance
from autocomplete.core import IResultHandler, ResultMatch, ScoreWeight


class RedundantPlacesIdFilter(IResultHandler):

    def handle(self, results: List[ResultMatch]) -> None:

        filteredResult: List[ResultMatch] = []
        hashSet: Set[int] = set()

        for r in sorted(results, key=lambda r: r.getScore(), reverse=True):  # O(n log(n))
            if r.owner.uid not in hashSet:  # O(1)
                hashSet.add(r.owner.uid)  # O(1)
                filteredResult.append(r)  # O(1)

        results.clear()
        results.extend(filteredResult)


# if the word is in chinese, or greek, we display exactly the word ("alternative name")
# that was a match in the same language.
# However, if it was a search using a "simple" alphabet, we return the
# "principal" name instead of the "alternative" name that was a match against the search
class PlaceDisplayNameMatchOverride(IResultHandler):

    def handle(self, results: List[ResultMatch]) -> None:

        def intersects(list1: list, list2: list) -> bool:
            return any(set(list1) & set(list2))

        override: bool = False

        for r in results:
            matchName: str = r.word.lower()
            asciiName: str = r.owner.nameAscii.lower()
            override = (matchName == asciiName or intersects(matchName.split(), asciiName.split()))

            if override:
                break

        if override:
            for r in results:
                r.word = r.owner.name


class PopulationSizeScoreWeightsGenerator(IResultHandler):

    def __init__(self, weight: float):
        self._weight = weight

    def handle(self, results: List[ResultMatch]) -> None:
        for r in results:
            populationScore: float = r.owner.population
            r.scores.append(ScoreWeight(populationScore, self._weight))


class CoordinatesScoreWeightsGenerator(IResultHandler):

    def __init__(self, latitude: Decimal, longitude: Decimal, weight: float):

        if latitude is None or longitude is None:
            raise ValueError("coordinates cannot be empty")

        self._referenceCoords: Tuple[Decimal, Decimal] = (latitude, longitude)
        self._weight = weight

    def handle(self, results: List[ResultMatch]) -> None:

        for r in results:
            # weights distance using Vincenty's distance, ellipsoid standard WGS-84. Time complexity O(1) amortized
            distanceScore: float = (-1) * geopy.distance.vincenty(self._referenceCoords, (r.owner.latitude, r.owner.longitude)).km
            r.scores.append(ScoreWeight(distanceScore, self._weight))
