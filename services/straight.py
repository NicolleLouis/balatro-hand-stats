from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.card_pile import CardPile

from constants.value import Value


class StraightService:
    @classmethod
    def cards_in_suit_from_low_value(cls, card_pile, low_value):
        next_values = cls.next_5_values(low_value)
        card_pile_distinct_values = card_pile.get_distinct_values()
        cards_in_suit = sum(1 for _ in next_values if _ in card_pile_distinct_values)
        return cards_in_suit

    @staticmethod
    def next_5_values(value) -> list:
        if value == 14:
            return [14, 2, 3, 4, 5]
        else:
            return list(range(value, value + 5))

    @staticmethod
    def next_6_values(value) -> list:
        if value == 14:
            return [14, 2, 3, 4, 5, 6]
        else:
            return list(range(value, value + 6))

    # Remove the straight_low_values where there is not enough card remaining to create a straight
    @classmethod
    def get_legal_low_values(cls, all_cards: CardPile):
        legal_low_values = []
        for low_value in Value.ALL_STRAIGHT_LOW_VALUES:
            location = cls.next_5_values(low_value)
            if all(all_cards.contains_at_least_a_value_card(value) for value in location):
                legal_low_values.append(low_value)
        return legal_low_values

    # Measure if the location of the straight starting at low value contains holes are successive values
    @classmethod
    def has_holes(cls, card_pile, low_value):
        next_values = cls.next_5_values(low_value)
        card_pile_distinct_values = card_pile.get_distinct_values()
        values_in_location = [value for value in next_values if value in card_pile_distinct_values]

        if len(values_in_location) == 0:
            return False

        # Replace Ace with 1 in case of low Ace
        if low_value == 14:
            values_in_location = [1 if value == 14 else value for value in values_in_location]

        first_value = min(values_in_location)
        last_value = max(values_in_location)
        return last_value - first_value != len(values_in_location) - 1
