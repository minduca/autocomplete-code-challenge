from typing import Tuple, List
from hello.core import Place, PlaceScore, IDb, IPlaceSearchQueryStrategy
from autocomplete.levenshteinTrie import LevenshteinTrie
from autocomplete.resultMatch import ResultMatch


class LevenshteinTrieSearchQueryStrategy(IPlaceSearchQueryStrategy):

    def __init__(self, db: IDb):
        self._db: IDb = db
        self._trie: LevenshteinTrie = None

    def search(self, query: str) -> Tuple[PlaceScore, ...]:

        reponse: Tuple[PlaceScore, ...] = ()

        if query:
            results: List[ResultMatch] = self._trie.search(query, maxCost=1)
            reponse = tuple(map(self._calculateScore, results))

        return reponse

    async def initAsync(self) -> None:

        places: Tuple[Place, ...] = await self._db.getAllAsync()
        self._trie = LevenshteinTrie()

        # high memory cost, but it pays out well in performance
        for place in places:
            allNames: List[Place] = place.getAllNames()
            for name in allNames:
                self._trie.insert(name, place)

    def _calculateScore(self, result: ResultMatch) -> PlaceScore:
        return PlaceScore(result.owner, score=result.cost)
