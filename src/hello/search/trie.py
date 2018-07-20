# Heavily inspired by Steve Hanov's algorithm (2011) that was released to the
# public domain and is available here :
# http://stevehanov.ca/blog/index.php?id=114

# Modifications that I made :
# Migrated global variables and methods into new class
# LevenshteinTrieSearch.
# MaxCost passed in the constructor instead of manuy levels of method
# parameter.
# Use of typings.
# added "owner" object to the trie node
from typing import List

# The Trie data structure keeps a set of words, organized with one node for
# each letter.  Each node has a branch for each letter that may follow it in
# the set of words.


class TrieNode:
    def __init__(self):
        self.word: str = None
        self.owner: object = None
        self.children: TrieNode = {}

    def insert(self, word: str, owner: object) -> int:
        node = self
        numberOfNewNodes: int = 0

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
                numberOfNewNodes += 1

            node = node.children[letter]

        node.word = word
        node.owner = owner

        return numberOfNewNodes


class ResultEntry:
    def __init__(self, word: str, owner: object, cost: int):
        self.word: str = word
        self.owner: object = owner
        self.cost: int = cost

    def __repr__(self):
        return "'{}' -> {} ({})".format(self.word, self.owner, self.cost)


class LevenshteinTrieSearch:

    def __init__(self, root: TrieNode, maxCost: int):
        self._root: TrieNode = root
        self._maxCost: int = maxCost

    # The search function returns a list of all words that are less than the
    # given maximum distance from the target word
    def search(self, word: str):

        # build first row
        currentRow: range = range(len(word) + 1)

        results: List[ResultEntry] = []

        # recursively search each branch of the trie
        for letter in self._root.children:
            self._searchRecursive(
                self._root.children[letter], letter, word, currentRow, results)

        return results

    # This recursive helper is used by the search function above.  It assumes
    # that the previousRow has been filled in already.
    def _searchRecursive(self,
                         node: TrieNode,
                         letter: TrieNode,
                         word: str,
                         previousRow: range,
                         results: List[ResultEntry]):

        columns: int = len(word) + 1
        currentRow: range = [previousRow[0] + 1]

        # Build one row for the letter, with a column for each letter in the
        # target
        # word, plus one for the empty string at column 0
        for column in range(1, columns):

            insertCost = currentRow[column - 1] + 1
            deleteCost = previousRow[column] + 1

            if word[column - 1] != letter:
                replaceCost = previousRow[column - 1] + 1
            else:
                replaceCost = previousRow[column - 1]

            currentRow.append(min(insertCost, deleteCost, replaceCost))

        # if the last entry in the row indicates the optimal cost is less than
        # the maximum cost, and there is a word in this trie node, then add it.
        if currentRow[-1] <= self._maxCost and node.word is not None:
            results.append(ResultEntry(
                node.word, node.owner, cost=currentRow[-1]))

        # if any entries in the row are less than the maximum cost, then
        # recursively search each branch of the trie
        if min(currentRow) <= self._maxCost:
            for l in node.children:
                self._searchRecursive(
                    node.children[l], l, word, currentRow, results)


# Source :
# https://stackoverflow.com/questions/46038694/implementing-a-trie-to-support-autocomplete-in-python
class TrieNode2:
    def __init__(self):
        self.end = False
        self.children = {}

    def all_words(self, prefix):
        if self.end:
            yield prefix

        for letter, child in self.children.items():
            yield from child.all_words(prefix + letter)


class Trie2:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for letter in word:
            node = curr.children.get(letter)
            if not node:
                node = TrieNode()
                curr.children[letter] = node
            curr = node

        curr.end = True

    def search(self, word):
        curr = self.root
        for letter in word:
            node = curr.children.get(letter)
            if not node:
                return False
            curr = node
        return curr.end

    def all_words_beginning_with_prefix(self, prefix):
        cur = self.root
        for c in prefix:
            cur = cur.children.get(c)
            if cur is None:
                return  # No words with given prefix

        yield from cur.all_words(prefix)
