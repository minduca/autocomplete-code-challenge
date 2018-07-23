import time
from hello.core import ResultMatch, Tuple


class PlaceSearchResult:

    def __init__(self, places: Tuple[ResultMatch, ...], start: time, end: time):
        self.places: Tuple[ResultMatch, ...] = places
        self.start: time = start
        self.end: time = end

    def getReponseTime(self) -> time:
        return self.end - self.start
