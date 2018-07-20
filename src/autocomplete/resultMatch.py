

class ResultMatch:
    def __init__(self, word: str, owner: object, cost: int):
        self.word: str = word
        self.owner: object = owner
        self.cost: int = cost

    def __repr__(self):
        return "'{}' -> {} ({})".format(self.word, self.owner, self.cost)
