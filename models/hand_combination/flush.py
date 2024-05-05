from constants.suit import Suit
from models.hand_combination.hand_combination import HandCombination


class Flush(HandCombination):
    def result(self):
        for suit in Suit.ALL_SUITS:
            if self.card_pile.number_of_card_with_suit(suit) >= 5:
                self.hand_description = f"{suit} Flush"
                return True
        return False

    def __str__(self):
        return "Flush"
