from constants.value import Value
from models.engine.straight.straight import StraightEngine
from services.straight import StraightService


class StraightV0Engine(StraightEngine):
    @classmethod
    def get_straight_score(cls, card_in_hand, remaining_cards, low_value):
        return StraightService.cards_in_suit_from_low_value(card_in_hand, low_value)

    @staticmethod
    def possible_values(card_in_hand, remaining_cards):
        return Value.ALL_STRAIGHT_LOW_VALUES
