import unittest
from typing import Tuple
from mock import MagicMock

from helloSuggestions.search.placeSearchEngine import PlaceSearchEngine
from helloSuggestions.search.placeSearchConfig import PlaceSearchConfig
from helloSuggestions.search.placeSearchStrategy import IPlaceSearchStrategy
from helloSuggestions.place import Place

class Test_placeSearchEngine(unittest.TestCase):
    
    def test_search_emptyStrategyResult_emptyCollection(self):
        #arrange
        query = 'auto'
        strategy: IPlaceSearchStrategy = self.createStrategy(result=())
        config = PlaceSearchConfig(maxNumberResults=10)
        engine = PlaceSearchEngine(strategy, config)

        #act
        result: Tuple[Place] = engine.search(query)

        #assert
        assert len(result) == 0
        assert strategy.search.called

    def test_search_emptyQuery_emptyCollection(self):
        #arrange
        query = ''
        strategy: IPlaceSearchStrategy = self.createStrategy(result=())
        config = PlaceSearchConfig(maxNumberResults=10)
        engine = PlaceSearchEngine(strategy, config)

        #act
        result: Tuple[Place] = engine.search(query)

        #assert
        self.assertEqual(len(result), 0)
        assert not strategy.search.called

    def test_search_invalidConfig_error(self):
        #arrange
        query = 'auto'
        strategy: IPlaceSearchStrategy = self.createStrategy(result=())
        config = PlaceSearchConfig(maxNumberResults=0)
        engine = PlaceSearchEngine(strategy, config)

        #act / assert
        self.assertRaises(ValueError, engine.search, query)

    def test_search_queryCaseEmptySpaces_queryParsed(self):
        #arrange
        query = ' Auto Complete  '
        strategy: IPlaceSearchStrategy = self.createStrategy(result=())
        config = PlaceSearchConfig(maxNumberResults=2)
        engine = PlaceSearchEngine(strategy, config)

        #act
        result: Tuple[Place] = engine.search(query)

        #assert
        strategy.search.assert_called_with('auto complete')

    def createStrategy(self, result: Tuple[Place]) -> IPlaceSearchStrategy:
        strategy = IPlaceSearchStrategy()
        strategy.search = MagicMock(return_value=result)
        return strategy
        