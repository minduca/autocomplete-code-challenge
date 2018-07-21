from typing import List
from .trieNode import TrieNode
from .levenshteinTracker import LevenshteinTracker
from .resultMatch import ResultMatch


class NodeMatch:
    def __init__(self, node: TrieNode, cost: int):
        self.node: TrieNode = node
        self.cost: int = cost

    def isPrefix(self) -> bool:
        return not self.node.isWholeWord()

    def __repr__(self):
        return "'{}' : {}".format(self.cost, self.node)


class LevenshteinTrie:

    def __init__(self):
        self._root: TrieNode = TrieNode(letter="", wordpath="")

    def insert(self, word: str, owner: object=None) -> None:
        self._root.insert(word.lower(), word, owner)

    # The search function returns a list of all words that are less than the
    # given maximum distance from the target word
    def search(self, word: str, maxCost: int) -> List[ResultMatch]:

        cumulativeResult: List[NodeMatch] = []
        tracker = LevenshteinTracker(word.lower(), maxCost)

        for char in self._root.children:
            self._searchBranch(
                self._root.children[char], cumulativeResult, tracker)

        return list(map(lambda n: ResultMatch(n.node.finalword, n.node.owner, n.cost), cumulativeResult))

    def _searchBranch(self, node: TrieNode, cumulativeResult: List[NodeMatch], tracker: LevenshteinTracker):

        tracker.appendLetterCost(node.letter, node.wordpath)

        if tracker.hasAnyCostAcceptable(node.wordpath):

            if tracker.isCurrentCostAcceptable(node.wordpath) and node.owner is not None:
                cumulativeResult.append(
                    NodeMatch(node, cost=tracker.getCurrentCost(node.wordpath)))

            for char in node.children:
                self._searchBranch(
                    node.children[char], cumulativeResult, tracker)
