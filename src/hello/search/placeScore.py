from hello.place import Place

class PlaceScore(object):
    def __init__(self, place: Place, score:float):
        self.place : Place = place
        self.score : float = score

