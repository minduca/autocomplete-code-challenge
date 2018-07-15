import asyncio
from hello.search.trie import TrieNode, LevenshteinTrieSearch, ResultEntry
from hello.core import Place, PlaceScore, IDb, IPlaceSearchQueryStrategy
from typing import Tuple, List

class LevenshteinTrieSearchQueryStrategy(IPlaceSearchQueryStrategy):
    
    def __init__(self, db: IDb):
        self._db : IDb = db
        self._trieSearch : LevenshteinTrieSearch = None

    def search(self, query: str) -> Tuple[PlaceScore, ...]:

        reponse : Tuple[PlaceScore, ...] = ()

        if query:
            queryParsed : str = query.lower()
            results: List[ResultEntry] = self._trieSearch.search(queryParsed)
            reponse = tuple(map(lambda result: PlaceScore(result.owner, score=0.5), results))

        return reponse

    async def initAsync(self):
        places : Tuple[Place, ...] = await self._db.getAllAsync()
        trie : Trie = self._loadTrie(places)
        self._trieSearch = LevenshteinTrieSearch(trie, maxCost=2)

    def _loadTrie(self, places: Tuple[Place, ...]) -> TrieNode:

        trie = TrieNode()
        
        # high memory cost, but it pays out very well in performance
        for place in places:
            allNames : List[Place] = place.getAllNames()
            for name in allNames:
                trie.insert(name.lower(), place)

        return trie
