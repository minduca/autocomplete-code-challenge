from typing import List, Dict


class LevenshteinTracker:

    def __init__(self, fullword: str, maxCost: int):
        self.fullword = fullword
        self._costmap: Dict[str, List[List[int]]] = {
            "": [range(len(fullword) + 1)]}
        self._maxCost: int = maxCost

    def appendLetterCost(self, char: str, wordpath: str) -> None:

        previousWordPath: str = wordpath[:-1]
        previousCostRow: List[int] = self._getCurrentCostRow(previousWordPath)
        self._appendNextCostRow(wordpath, previousCostRow)
        currentCostRow: List[int] = self._getCurrentCostRow(wordpath)

        for column in range(1, self._getNumberColumns()):

            estMatchChar: bool = self.fullword[column - 1] == char
            insertCost: int = currentCostRow[column - 1] + 1
            deleteCost: int = previousCostRow[column] + 1
            replaceCost: int = previousCostRow[column -
                                               1] + (0 if estMatchChar else 1)
            finalCost: int = min(insertCost, deleteCost, replaceCost)

            currentCostRow.append(finalCost)

    def _getNumberColumns(self) -> int:
        return len(self.fullword) + 1

    def isCurrentCostAcceptable(self, wordpath: str) -> bool:
        currentCost: int = self.getCurrentCost(wordpath)
        return currentCost <= self._maxCost

    def hasAnyCostAcceptable(self, wordpath: str) -> bool:
        currentCostRow: List[int] = self._getCurrentCostRow(wordpath)
        return any(cost <= self._maxCost for cost in currentCostRow)

    def getCurrentCost(self, wordpath: str) -> int:
        currentCostRow: List[int] = self._getCurrentCostRow(wordpath)
        return currentCostRow[-1]

    def _appendNextCostRow(self, wordpath: str, previousCostRow: List[int]) -> None:

        if wordpath in self._costmap:
            raise ValueError("wat?")

        self._costmap[wordpath] = [[previousCostRow[0] + 1]]

    def _getCurrentCostRow(self, wordpath: str) -> List[int]:
        return self._costmap[wordpath][-1]
