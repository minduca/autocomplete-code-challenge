import unittest
from typing import Tuple, List
from unittest.mock import MagicMock
from autocomplete.levenshteinTrie import LevenshteinTrie
from autocomplete.resultMatch import ResultMatch

class Test_LevenshteinTrie(unittest.TestCase):

    def test_emptytree_emptyresult(self):
        
        self.search_DataDrivenTest(
            database=(), 
            query="any", maxCost=3, 
            expectedResult=[])

    def test_search_partialWord_approximatedWordsReturned(self):
        
        self.search_DataDrivenTest(
            database=("Batman", "Robin", "Batman & Robin", "Wonder Woman", "Robin Hood", "Batgirl & Robin"), 
            query="bat man", maxCost=3, 
            expectedResult=["Batman", "Batman & Robin"])

    def test_search_similarWord_approximatedWordsReturned(self):
        
        self.search_DataDrivenTest(
            database=("Batman", "Robin", "Batman & Robin", "Wonder Woman", "Robin Hood", "Batgirl & Robin"), 
            query="bat man & rboin", maxCost=3, 
            expectedResult=["Batman & Robin"])

    def search_DataDrivenTest(self, database: Tuple[str,...], query:str, maxCost: int, expectedResult: Tuple[str,...]) -> List[ResultMatch]:
        
        #arrange
        trie: LevenshteinTrie = self.createTrie(database)

        #act
        result: List[ResultMatch] = trie.search(query, maxCost)

        #assert
        assert len(result) == len(expectedResult)
        assert all(r.word in expectedResult for r in result)

    def createTrie(self, words: Tuple[str, ...]) -> LevenshteinTrie:
        
        trie = LevenshteinTrie()

        for word in words:
            trie.insert(word)

        return trie