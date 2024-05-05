from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from constants.suit import Suit
from models.card_pile import CardPile

if TYPE_CHECKING:
    from models.deck_setting import DeckSetting


class Deck:
    def __init__(self, deck_settings: Optional[DeckSetting] = None):
        self.pile: Optional[CardPile] = None
        self.deck_settings = deck_settings

        self.fill_deck()

        if self.deck_settings:
            self.deck_settings.perform(self.pile)

    def fill_deck(self):
        raise NotImplementedError

    def __str__(self):
        return f"{len(self.pile)} cards in deck"

    def suit_repartition(self):
        suit_repartition = {}
        for suit in Suit.ALL_SUITS:
            suit_repartition[suit] = self.pile.number_of_card_with_suit(suit)
        return suit_repartition

    def value_repartition(self):
        value_repartition = {}
        for value in range(2, 15):
            value_repartition[value] = self.pile.number_of_card_with_value(value)
        return value_repartition
