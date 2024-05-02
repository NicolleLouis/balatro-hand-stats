from constants.value import Value


class Card:
    def __init__(self, suit: str, value: int):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{Value.translate(self.value)} of {self.suit}"
