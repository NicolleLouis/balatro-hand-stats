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
