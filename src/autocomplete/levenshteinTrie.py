from typing import List
from .trieNode import TrieNode
from .levenshteinTracker import LevenshteinTracker
from .core import IResultHandler, ResultMatch, ScoreWeight

# O(log(n))

# Trie data structure(aka prefix tree, radix tree) that also implements word approximation by computing the Levenshtein distance between its nodes.


class LevenshteinTrie:

    def __init__(self, fixedPrefixSize: int, scoreWeight: float):
        self._root: TrieNode = TrieNode(letter="", wordpath="")
        self._fixedPrefixSize: int = fixedPrefixSize if fixedPrefixSize > 0 else 1
        self._scoreWeight: float = scoreWeight if scoreWeight > 0 else 1

    def insert(self, word: str, owner: object=None) -> None:
        self._root.insert(word.lower(), word, owner)

    def search(self, word: str, maxCost: int, resulthandler: IResultHandler = None) -> List[ResultMatch]:

        cumulativeResult: List[ResultMatch] = []
        wordparsed: str = word.lower()

        tracker = LevenshteinTracker(wordparsed, maxCost)

        potentialPrefixesNodes: List[TrieNode] = self._navigateToPotentialPrefixes(wordparsed, tracker)

        if potentialPrefixesNodes:
            for prefixNode in potentialPrefixesNodes:
                self._searchBranch(prefixNode, cumulativeResult, tracker)

        if resulthandler is not None and any(cumulativeResult):
            resulthandler.handle(cumulativeResult)

        # For only the words that match the query, it sorts by score with O(n log(n))
        return sorted(cumulativeResult, key=lambda r: r.getScore(), reverse=True)

    def _navigateToPotentialPrefixes(self, fullword: str, tracker: LevenshteinTracker) -> List[TrieNode]:

        # filter nodes in the Trie that are similars to the word being search.
        # It uses some approximation that considers that the first letter of the
        # query is always right, but the other letters might be misplaced by one position.

        potentialPrefixesNodes: List[TrieNode] = []
        approximatePrefixes: List[str] = []

        if len(fullword) >= self._fixedPrefixSize:
            prefix = fullword[0:self._fixedPrefixSize+1]

            for idx in range(1, len(prefix)):
                approximatePrefix = prefix[0:idx] + (prefix[idx:idx+2][::-1]) + ("" if (idx+2) > len(prefix) else prefix[idx+2:])
                approximatePrefixes.append(approximatePrefix[0:self._fixedPrefixSize])

        if approximatePrefixes:
            approximatePrefixes = list(set(approximatePrefixes))
            for approximatePrefix in approximatePrefixes:
                prefixNode: TrieNode = self._navigateTo(approximatePrefix, tracker)
                if prefixNode is not None:
                    potentialPrefixesNodes.append(prefixNode)

        return potentialPrefixesNodes

    def _navigateTo(self, wordpath: str, tracker: LevenshteinTracker) -> TrieNode:

        # Returns the exact node that corresponds to the word path

        node: TrieNode = self._root

        if wordpath:
            node = self._root

            for idx, char in enumerate(wordpath):
                node = node.children.get(char)
                if node is None:
                    break

        if node is not None:
            for idx, char in enumerate(wordpath):
                partialWordPath = wordpath[0:idx + 1]
                if idx < (len(wordpath) - 1) and not tracker.isPathCalculated(partialWordPath):
                    tracker.appendLetterCost(char, partialWordPath)

        return node

    def _searchBranch(self, node: TrieNode, cumulativeResult: List[ResultMatch], tracker: LevenshteinTracker):

        tracker.appendLetterCost(node.letter, node.wordpath)

        if tracker.hasAnyCostAcceptable(node.wordpath):

            if tracker.isCurrentCostAcceptable(node.wordpath):

                cost: int = tracker.getCurrentCost(node.wordpath)

                if node.isWholeWord():
                    self._addOrUpdateResult(cumulativeResult, node, cost)
                elif tracker.isNodeSameLevelThanWord(node.wordpath):
                    for childNode in node.getChildrenWholeWordsNodes():
                        self._addOrUpdateResult(cumulativeResult, childNode, cost)

            for char in node.children:
                self._searchBranch(node.children[char], cumulativeResult, tracker)

    def _addOrUpdateResult(self, cumulativeResult: List[ResultMatch], node: TrieNode, cost: int) -> None:

        newResult = ResultMatch(node.finalword, node.owner)
        costScore: float = (-1) * cost
        newResult.scores.append(ScoreWeight(costScore, self._scoreWeight))
        resultAlreadyExists: bool = False

        for idx, existingResult in enumerate(cumulativeResult):

            resultAlreadyExists = existingResult.isSame(newResult)
            if resultAlreadyExists:
                cumulativeResult[idx] = newResult
                break

        if not resultAlreadyExists:
            cumulativeResult.append(newResult)
