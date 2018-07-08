from typing import Tuple
from .place import Place

# Interface for data access
class IDb(object):
    def data(self) -> Tuple[Place]:
        raise NotImplementedError

# Interface for search algorithms
class IPlaceSearchStrategy(object):
    def search(self, query) -> Tuple[Place]:
        raise NotImplementedError()