from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from models.card_pile import CardPile
    from models.hand_combination.hand_combination import HandCombination


class Engine:
    def __init__(self, hand_combination: Type[HandCombination]):
        self.hand_combination = hand_combination

    def choose_discard(self, card_in_hand: CardPile, remaining_cards: CardPile) -> CardPile:
        raise NotImplementedError

    def result(self, card_pile: CardPile) -> str:
        return self.hand_combination(card_pile).result()
