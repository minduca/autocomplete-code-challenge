import unittest
from typing import Tuple
from unittest.mock import MagicMock

from hello.search.placeSearchEngine import PlaceSearchEngine
from hello.search.placeSearchConfig import PlaceSearchConfig
from hello.search.placeSearchResult import PlaceSearchResult
from hello.core import IPlaceSearchQueryStrategy, PlaceScore

class Test_placeSearchEngine(unittest.TestCase):
    
    def test_search_emptyStrategyResult_emptyCollection(self):
        #arrange
        query:str = 'auto'
        strategy: IPlaceSearchQueryStrategy = self.createStrategy(result=())
        config = PlaceSearchConfig(maxNumberResults=10)
        engine = PlaceSearchEngine(strategy, config)

        #act
        result: PlaceSearchResult = engine.search(query)

        #assert
        assert len(result.places) == 0
        assert strategy.search.called

    def test_search_emptyQuery_emptyCollection(self):
        #arrange
        query:str = ''
        strategy: IPlaceSearchQueryStrategy = self.createStrategy(result=())
        config = PlaceSearchConfig(maxNumberResults=10)
        engine = PlaceSearchEngine(strategy, config)

        #act
        result: PlaceSearchResult = engine.search(query)

        #assert
        assert len(result.places) == 0
        assert not strategy.search.called

    def test_search_invalidConfig_error(self):
        #arrange
        query:str = 'auto'
        strategy: IPlaceSearchQueryStrategy = self.createStrategy(result=())
        config = PlaceSearchConfig(maxNumberResults=0)
        engine = PlaceSearchEngine(strategy, config)

        #act / assert
        self.assertRaises(ValueError, engine.search, query)

    def test_search_queryTrailingSpaces_queryParsed(self):
        #arrange
        query:str = ' Auto Complete  '
        strategy: IPlaceSearchQueryStrategy = self.createStrategy(result=())
        config = PlaceSearchConfig(maxNumberResults=2)
        engine = PlaceSearchEngine(strategy, config)

        #act
        result: PlaceSearchResult = engine.search(query)

        #assert
        strategy.search.assert_called_with('Auto Complete')

    def createStrategy(self, result: Tuple[PlaceScore]) -> IPlaceSearchQueryStrategy:
        strategy = IPlaceSearchQueryStrategy()
        strategy.search = MagicMock(return_value=result)
        return strategy
        