#Separate files for interfaces because the dependencies here are much thinner,
#easing imports on other scripts by mitigating the risk of cyclic references of
#scripts

#if this file becomes too big, we can split it content in different files, but under the same module name.

from typing import Tuple, List
from .place import Place
from hello.search.placeScore import PlaceScore

# Interface for data access
class IDb(object):
    def getAllAsync(self) -> Tuple[Place, ...]:
        raise NotImplementedError

# interface for reading from a data source
class IDataReader(object):
    def readAll() -> List[Place]:
        raise NotImplementedError()

# Interface for search algorithms
class IPlaceSearchQueryStrategy(object):
    def search(self, query) -> Tuple[PlaceScore, ...]:
        raise NotImplementedError()