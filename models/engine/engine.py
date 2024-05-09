from __future__ import annotations

from models.card_pile import CardPile

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from models.hand_combination.hand_combination import HandCombination


class Engine:
    def __init__(self, hand_combination: Type[HandCombination]):
        self.hand_combination = hand_combination

    def discard(self, card_in_hand: CardPile, remaining_cards: CardPile) -> CardPile:
        if self.result(card_in_hand):
            return CardPile()

        discarded_cards = self.get_discard_cards(card_in_hand, remaining_cards)
        return discarded_cards.pick_cards(5)

    def get_discard_cards(self, card_in_hand: CardPile, remaining_cards: CardPile) -> CardPile:
        raise NotImplementedError

    def result(self, card_pile: CardPile) -> str:
        return self.hand_combination(card_pile).result()
