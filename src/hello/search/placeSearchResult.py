from hello.core import Place, PlaceScore, Tuple
import time

class PlaceSearchResult(object):
    
    def __init__(self, places: Tuple[PlaceScore, ...], start: time, end: time):
        self.places : Tuple[PlaceScore, ...] = places
        self.start : time = start
        self.end : time = end

    def getReponseTime(self) -> time:
        return (self.end - self.start)

