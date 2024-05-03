from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.card_pile import CardPile


class HandCombination:
    def __init__(self, card_pile: CardPile):
        self.card_pile = card_pile
        self.hand_description = ""

    def result(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError
