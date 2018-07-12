from typing import Tuple, Callable
from helloSuggestions.core import IDb, IPlaceSearchStrategy, Place

class VeryDummyPlaceSearchStrategy(IPlaceSearchStrategy):
    
    def __init__(self, db: IDb):
        self._db : IDb = db

    def search(self, query) -> Tuple[Place, ...]:

        reponse : Tuple[Place, ...] = ()

        if query:
            isMatch : Callable[[Place], bool] = lambda place: place.name.lower().startswith(query)
            reponse = tuple(filter(isMatch, self._db.data()))

        return reponse