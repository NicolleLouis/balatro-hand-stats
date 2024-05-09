from models.engine.straight.straight import StraightEngine
from services.straight import StraightService


class StraightV1Engine(StraightEngine):
    @staticmethod
    def get_straight_score(card_in_hand, low_value):
        return StraightService.cards_in_suit_from_low_value(card_in_hand, low_value)

    @staticmethod
    def possible_values(card_in_hand, remaining_cards):
        all_cards = card_in_hand + remaining_cards
        return StraightService.get_legal_low_values(all_cards)
