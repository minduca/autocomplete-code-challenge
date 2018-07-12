from typing import Tuple, Callable
from helloSuggestions.core import IDb, IPlaceSearchStrategy, Place, PlaceScore


class VeryDummyPlaceSearchStrategy(IPlaceSearchStrategy):
    
    def __init__(self, db: IDb):
        self._db : IDb = db

    def search(self, query) -> Tuple[PlaceScore, ...]:

        reponse : Tuple[PlaceScore, ...] = ()

        if query:
            isMatch : Callable[[Place], bool] = lambda place: place.name.lower().startswith(query)
            places = filter(isMatch, self._db.data())
            reponse = tuple(map(lambda place: PlaceScore(place, score=0.5), places))

        return reponse