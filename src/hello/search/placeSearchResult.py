import time
from hello.core import PlaceScore, Tuple

class PlaceSearchResult:

    def __init__(self, places: Tuple[PlaceScore, ...], start: time, end: time):
        self.places : Tuple[PlaceScore, ...] = places
        self.start : time = start
        self.end : time = end

    def getReponseTime(self) -> time:
        return self.end - self.start
