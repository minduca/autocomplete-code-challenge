from typing import Dict


class TrieNode:
    def __init__(self, letter: str, wordpath: str):
        self.letter: str = letter
        self.wordpath: str = wordpath
        self.finalword: str = None
        self.owner: object = None
        self.children: Dict[str, TrieNode] = {}

    def insert(self, wordparsed: str, finalword: str, owner: object=None) -> None:
        leaf: TrieNode = self._createOrGetLeaf(wordparsed)
        leaf.finalword = finalword
        leaf.owner = owner if owner is not None else finalword

    def isWholeWord(self) -> bool:
        return self.owner is not None

    def _createOrGetLeaf(self, fullword: str):

        node = self

        for char in fullword:
            if char not in node.children:
                node.children[char] = TrieNode(char, node.wordpath + char)

            node = node.children[char]

        return node

    def __repr__(self):
        return '>'.join(self.wordpath) + " (is whole word)" if self.isWholeWord() else ""
