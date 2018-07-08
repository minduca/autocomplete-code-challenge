from typing import Tuple
from .place import Place
from .db import IDb
from .core import IPlaceSearchStrategy
from typing import Callable # <- This represents a "hint" typed function

class VeryDummyPlaceSearchStrategy(IPlaceSearchStrategy):
    
    def __init__(self, db: IDb):
        self.db = db

    def search(self, query) -> Tuple[Place]:

        reponse: Tuple[Place] = ()

        if query:
            isMatch: Callable[[Place], bool] = lambda place: place.name.lower().startswith(query)
            reponse = tuple(filter(isMatch, self.db.data()))

        return reponse