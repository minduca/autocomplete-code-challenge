from typing import Tuple, List
from autocomplete.core import IResultHandler
from autocomplete.levenshteinTrie import LevenshteinTrie
from hello.core import Place, ResultMatch, IDb, IPlaceSearchQueryStrategy


class LevenshteinTrieSearchQueryStrategy(IPlaceSearchQueryStrategy):

    def __init__(self, db: IDb, scoreWeightQuerySearch: int):

        if scoreWeightQuerySearch <= 0:
            raise ValueError("The weight of the result returned by the query search must be superior to zero")

        self._db: IDb = db
        self._scoreWeightQuerySearch: int = scoreWeightQuerySearch
        self._trie: LevenshteinTrie = None

    def search(self, query: str, resulthandler: IResultHandler) -> List[ResultMatch]:
        return self._trie.search(query, maxCost=3, resulthandler=resulthandler)

    async def initAsync(self) -> None:
        places: Tuple[Place, ...] = await self._db.getAllAsync()
        self._initTrie(places)

    def _initTrie(self, places: Tuple[Place, ...]):
        self._trie = LevenshteinTrie(fixedPrefixSize=2, scoreWeight=self._scoreWeightQuerySearch)

        # high memory cost, but it pays out in performance
        for place in places:
            allNames: List[Place] = place.getAllNames()
            for name in allNames:
                self._trie.insert(name, place)
