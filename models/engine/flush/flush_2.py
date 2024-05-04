from __future__ import annotations

from models.engine.engine import Engine
from models.hand_combination.flush import Flush
from models.card_pile import CardPile
from services.flush_engine import FlushEngineService

"""
Third version of the Flush engine.
New rule: 
To pick the best suit, the engine will consider the suit with the most cards in hand and the repartition of the draw 
pile
"""


class FlushV2Engine(Engine):
    def __init__(self):
        super().__init__(Flush)

    def get_discard_cards(self, card_in_hand: CardPile, remaining_cards: CardPile) -> CardPile:
        best_suit = FlushEngineService.get_best_suit(card_in_hand, remaining_cards)
        wrong_suit_cards = FlushEngineService.get_wrong_suit_cards(card_in_hand, best_suit)
        return wrong_suit_cards
