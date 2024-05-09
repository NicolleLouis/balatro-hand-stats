from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.card_pile import CardPile

from constants.value import Value


class StraightService:
    @classmethod
    def cards_in_suit_from_low_value(cls, card_pile, low_value):
        next_values = cls.next_5_values(low_value)
        cards_in_suit = 0
        for _ in next_values:
            if card_pile.contains_at_least_a_value_card(_):
                cards_in_suit += 1
        return cards_in_suit

    @staticmethod
    def next_5_values(value) -> list:
        if value == 14:
            return [14, 2, 3, 4, 5]
        else:
            return list(range(value, value + 5))

    # Remove the straight_low_values where there is not enough card remaining to create a straight
    @classmethod
    def get_legal_low_values(cls, all_cards: CardPile):
        legal_low_values = []
        for low_value in Value.ALL_STRAIGHT_LOW_VALUES:
            location = cls.next_5_values(low_value)
            if all(all_cards.contains_at_least_a_value_card(value) for value in location):
                legal_low_values.append(low_value)
        return legal_low_values
