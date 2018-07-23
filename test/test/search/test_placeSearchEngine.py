import unittest
from typing import Tuple
from unittest.mock import MagicMock

from hello.search.placeSearchEngine import PlaceSearchEngine
from hello.search.placeSearchResult import PlaceSearchResult
from hello.core import IPlaceSearchQueryStrategy, ResultMatch

class Test_PlaceSearchEngine(unittest.TestCase):
    
    def test_search_emptyStrategyResult_emptyCollection(self):
        #arrange
        query:str = 'auto'
        strategy: IPlaceSearchQueryStrategy = self.createStrategy(result=())
        engine: PlaceSearchEngine = self.createEngine(strategy)
        strategy = engine._searchStrategy

        #act
        result: PlaceSearchResult = engine.search(query)

        #assert
        assert len(result.places) == 0
        assert strategy.search.called

    def test_search_emptyQuery_emptyCollection(self):
        #arrange
        query:str = ''
        strategy: IPlaceSearchQueryStrategy = self.createStrategy(result=())
        engine: PlaceSearchEngine = self.createEngine(strategy)

        #act
        result: PlaceSearchResult = engine.search(query)

        #assert
        assert len(result.places) == 0
        assert not strategy.search.called

    def test_search_invalidConfig_error(self):
        #arrange
        query:str = 'auto'
        strategy: IPlaceSearchQueryStrategy = self.createStrategy(result=())

        #act / assert
        self.assertRaises(ValueError, PlaceSearchEngine, strategy, 0, 1, 1)


    def createEngine(self, strategy: IPlaceSearchQueryStrategy) -> PlaceSearchEngine:
        return PlaceSearchEngine(strategy, 
                                 maxNumberResults=10, 
                                 scoreWeightPopulationSize=1,
                                 scoreWeightCoordinatesDistance=1)

    def createStrategy(self, result: Tuple[ResultMatch]) -> IPlaceSearchQueryStrategy:
        strategy = IPlaceSearchQueryStrategy()
        strategy.search = MagicMock(return_value=result)
        return strategy
       
    #TODO add missing tests