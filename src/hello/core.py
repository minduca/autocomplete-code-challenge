# Separate files for interfaces because the dependencies here are much thinner,
# easing imports on other scripts by mitigating the risk of cyclic references of
# scripts

# if this file becomes too big, we can split it content in different files, but
# under the same module name.
from typing import Tuple, List
from hello.place import Place
from autocomplete.core import IResultHandler, ResultMatch

# Interface for data access


class IDb:
    def getAllAsync(self) -> Tuple[Place, ...]:
        raise NotImplementedError()

# interface for reading from a data source


class IDataReader:
    def readAll(self) -> List[Place]:
        raise NotImplementedError()

# Handles the *query* part of the search


class IPlaceSearchQueryStrategy:
    def search(self, query: str, resulthandler: IResultHandler) -> List[ResultMatch]:
        raise NotImplementedError()
