from typing import Tuple
from helloSuggestions.place import Place
from helloSuggestions.db import IDb
from typing import Callable # <- This represents a "hint" typed function

# Interface for search algorithms
class IPlaceSearchStrategy(object):
    def search(self, query) -> Tuple[Place]:
        raise NotImplementedError()

class VeryDummyPlaceSearchStrategy(IPlaceSearchStrategy):
    
    def __init__(self, db: IDb):
        self.db = db

    def search(self, query) -> Tuple[Place]:

        reponse: Tuple[Place] = ()

        if query:
            isMatch: Callable[[Place], bool] = lambda place: place.name.lower().startswith(query)
            reponse = tuple(filter(isMatch, self.db.data()))

        return reponse