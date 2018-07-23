
from typing import List
from .core import IResultHandler, ResultMatch, ScoreWeight


class CompositeHandlers(IResultHandler):

    def __init__(self, handlers: List[IResultHandler]):
        self._handlers = handlers

    def handle(self, results: List[ResultMatch]) -> None:
        if any(results):
            for handler in self._handlers:
                handler.handle(results)


# Scales the score to the range 0-1 and aggregates all the scores
# onto a single value taking the weights of each score into account.
class ZeroToOneScaleScoreAggregator(IResultHandler):

    def handle(self, results: List[ResultMatch]) -> None:

        normalizer = ZeroToOneScaleScoreNormalizer()

        normalizer.handle(results)
        self._aggregateScores(results)
        normalizer.handle(results)

    def _aggregateScores(self, results: List[ResultMatch]) -> None:
        for r in results:
            aggregatedScore = ScoreWeight(r.getScore(), weight=1)
            r.scores.clear()
            r.scores.append(aggregatedScore)

# Scales the score to the range 0-1


class ZeroToOneScaleScoreNormalizer(IResultHandler):

    def handle(self, results: List[ResultMatch]) -> None:

        numberOfScores: int = len(results[0].scores)

        for idx in range(0, numberOfScores):
            minCost: float = min(r.scores[idx].score for r in results)
            maxCost: float = max(r.scores[idx].score for r in results)
            diffMaxMinCost = float(maxCost - minCost)

            if minCost < 0 or maxCost > 1:
                for r in results:
                    scaledScore = 1 if diffMaxMinCost == 0 else float(r.scores[idx].score - minCost) / diffMaxMinCost
                    r.scores[idx].score = scaledScore
