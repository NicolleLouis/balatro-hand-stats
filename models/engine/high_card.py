from __future__ import annotations

from models.engine.engine import Engine
from models.card_pile import CardPile
from models.hand_combination.high_card import HighCard


class HighCardEngine(Engine):
    def __init__(self):
        super().__init__(HighCard)

    def choose_discard(self, card_in_hand: CardPile, remaining_cards: CardPile) -> CardPile:
        return card_in_hand.pick_cards(1)
