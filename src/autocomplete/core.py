from typing import List


class ResultMatch:
    def __init__(self, word: str, owner: object):
        self.word: str = word
        self.owner: object = owner
        self.scores: List[ScoreWeight] = []

    def isSame(self, otherResult) -> bool:
        return self.word == otherResult.word and self.owner == otherResult.owner

    def getScore(self) -> float:
        return sum(map(lambda s: s.calculate(), self.scores))

    def __repr__(self):
        return "'{}' : {}".format(self.word, self.getScore())


class ScoreWeight:

    def __init__(self, score: float, weight: float):
        self.score: float = score
        self.weight: float = weight

    def calculate(self) -> float:
        return float(self.score) * float(self.weight)


class IResultHandler:
    def handle(self, results: List[ResultMatch]) -> None:
        raise NotImplementedError()
