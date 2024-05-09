from models.engine.straight.straight import StraightEngine
from services.straight import StraightService


class StraightV3Engine(StraightEngine):
    @classmethod
    def get_straight_score(cls, card_in_hand, remaining_cards, low_value):
        score = StraightService.cards_in_suit_from_low_value(card_in_hand, low_value)
        if StraightService.has_holes(card_in_hand, low_value):
            score -= 0.5
        outs_probability = cls.add_outs_probability(card_in_hand, remaining_cards, low_value)
        score += outs_probability / 2
        return score

    @classmethod
    def add_outs_probability(cls, card_in_hand, remaining_cards, low_value):
        if len(remaining_cards) == 0:
            return 0
        outs_number = 0
        missing_values = cls.missing_values(card_in_hand, low_value)
        for value in missing_values:
            outs_number += remaining_cards.number_of_card_with_value(value)
        outs_probability = outs_number / len(remaining_cards)
        return outs_probability

    @classmethod
    def missing_values(cls, card_pile, low_value, should_take_6=False):
        if should_take_6:
            next_values = StraightService.next_6_values(low_value)
        else:
            next_values = StraightService.next_5_values(low_value)
        card_pile_distinct_values = card_pile.get_distinct_values()
        missing_values = [value for value in next_values if value not in card_pile_distinct_values]
        if not should_take_6 and cls.should_take_6(card_pile, missing_values, low_value):
            return cls.missing_values(card_pile, low_value, should_take_6=True)
        return missing_values

    # Function is computing if we should consider a 6th out in the score computation.
    # This case is reached if we have 4 consecutive cards and the last one is not missing
    @staticmethod
    def should_take_6(card_pile, missing_values, low_value):
        if StraightService.has_holes(card_pile, low_value):
            return False
        if len(missing_values) > 1:
            return False
        next_values = StraightService.next_5_values(low_value)
        return next_values[-1] != missing_values[-1]

    @staticmethod
    def possible_values(card_in_hand, remaining_cards):
        all_cards = card_in_hand + remaining_cards
        return StraightService.get_legal_low_values(all_cards)
