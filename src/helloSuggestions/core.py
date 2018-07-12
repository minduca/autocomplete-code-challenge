#Separate files for interfaces because the dependencies here are much thinner,
#easing imports on other scripts by mitigating the risk of cyclic references of
#scripts

#if this file becomes too big, we can split it content in different files, but under the same module name.

from typing import Tuple
from .place import Place

# Interface for data access
class IDb(object):
    def data(self) -> Tuple[Place, ...]:
        raise NotImplementedError

# interface for reading from a data source
class IDataReader(object):
    def readAll() -> list:
        raise NotImplementedError()

# Interface for search algorithms
class IPlaceSearchStrategy(object):
    def search(self, query) -> Tuple[Place, ...]:
        raise NotImplementedError()