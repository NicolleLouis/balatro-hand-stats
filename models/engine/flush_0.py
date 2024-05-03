from __future__ import annotations

from models.engine.engine import Engine
from models.hand_combination.flush import Flush
from models.card_pile import CardPile
from services.flush_engine import FlushEngineService

"""
First version of the Flush engine.
This engine will discard the cards that are not in the suit with the most cards in the hand.
No further logic is implemented.
"""


class FlushV0Engine(Engine):
    def __init__(self):
        super().__init__(Flush)

    def get_discard_cards(self, card_in_hand: CardPile, remaining_cards: CardPile) -> CardPile:
        best_suit = FlushEngineService.get_legal_suit_with_most_cards_in_hand(card_in_hand)
        wrong_suit_cards = FlushEngineService.get_wrong_suit_cards(card_in_hand, best_suit)
        return wrong_suit_cards
