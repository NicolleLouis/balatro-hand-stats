from constants.suit import Suit
from models.hand_combinations.base import HandCombinations


class Flush(HandCombinations):
    def result(self):
        for suit in Suit.ALL_SUITS:
            if self.card_pile.card_by_suit(suit) >= 5:
                self.hand_description = f"{suit} Flush"
                return True
        return False

    def __str__(self):
        return "Flush"
