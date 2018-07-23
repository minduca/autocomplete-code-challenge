from typing import List, Dict


class LevenshteinTracker:

    def __init__(self, fullword: str, maxCost: int):

        if not fullword:
            raise ValueError("fullword")

        self._fullword = fullword
        self._costmap: Dict[str, List[List[int]]] = {"": [range(len(self._fullword) + 1)]}
        self._maxCost: int = maxCost
        self._numberOfColumns = len(self._fullword) + 1

    def appendLetterCost(self, char: str, wordpath: str) -> None:

        previousWordPath: str = wordpath[:-1]
        previousCostRow: List[int] = self._getCurrentCostRow(previousWordPath)
        self._appendNextCostRow(wordpath, previousCostRow)
        currentCostRow: List[int] = self._getCurrentCostRow(wordpath)

        for idx in range(1, self._numberOfColumns):

            estMatchChar: bool = self._fullword[idx - 1] == char
            insertCost: int = currentCostRow[idx - 1] + 1
            deleteCost: int = previousCostRow[idx] + 1
            replaceCost: int = previousCostRow[idx - 1] + (0 if estMatchChar else 1)
            finalCost: int = min(insertCost, deleteCost, replaceCost)

            currentCostRow.append(finalCost)

    def isCurrentCostAcceptable(self, wordpath: str) -> bool:
        currentCost: int = self.getCurrentCost(wordpath)
        return currentCost <= self._maxCost

    def isNodeSameLevelThanWord(self, wordpath: str) -> bool:
        return len(wordpath) == len(self._fullword)  # O(1)

    def hasAnyCostAcceptable(self, wordpath: str) -> bool:
        currentCostRow: List[int] = self._getCurrentCostRow(wordpath)
        return any(cost <= self._maxCost for cost in currentCostRow)

    def getCurrentCost(self, wordpath: str) -> int:
        currentCostRow: List[int] = self._getCurrentCostRow(wordpath)
        return currentCostRow[-1]

    def isPathCalculated(self, wordpath: str) -> bool:
        return wordpath in self._costmap

    def _appendNextCostRow(self, wordpath: str, previousCostRow: List[int]) -> None:

        if self.isPathCalculated(wordpath):
            raise ValueError("The path given already was calculated")

        self._costmap[wordpath] = [[previousCostRow[0] + 1]]

    def _getCurrentCostRow(self, wordpath: str) -> List[int]:
        return self._costmap[wordpath][-1]
