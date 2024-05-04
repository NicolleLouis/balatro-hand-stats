from __future__ import annotations

from models.engine.engine import Engine
from models.hand_combination.flush import Flush
from models.card_pile import CardPile
from services.flush_engine import FlushEngineService

"""
Second version of the Flush engine.
New rule: 
If a suit doesn't have enough card left to make a flush, the engine will discard all cards of that suit.
"""


class FlushV1Engine(Engine):
    def __init__(self):
        super().__init__(Flush)

    def get_discard_cards(self, card_in_hand: CardPile, remaining_cards: CardPile) -> CardPile:
        legal_suits = FlushEngineService.get_legal_suits(card_in_hand, remaining_cards)
        best_suit = FlushEngineService.get_legal_suit_with_most_cards_in_hand(card_in_hand, legal_suits)
        wrong_suit_cards = FlushEngineService.get_wrong_suit_cards(card_in_hand, best_suit)
        return wrong_suit_cards
