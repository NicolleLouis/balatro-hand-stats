from typing import Optional

from constants.suit import Suit
from models.card_pile import CardPile


class Deck:
    def __init__(self):
        self.pile: Optional[CardPile] = None
        self.fill_deck()

    def fill_deck(self):
        raise NotImplementedError

    def __str__(self):
        return f"{len(self.pile)} cards in deck"

    def suit_repartition(self):
        suit_repartition = {}
        for suit in Suit.ALL_SUITS:
            suit_repartition[suit] = self.pile.card_by_suit(suit)
        return suit_repartition

    def value_repartition(self):
        value_repartition = {}
        for value in range(2, 15):
            value_repartition[value] = self.pile.card_by_value(value)
        return value_repartition
