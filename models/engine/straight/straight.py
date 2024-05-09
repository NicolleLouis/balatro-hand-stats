from models.card_pile import CardPile
from models.engine.engine import Engine
from models.hand_combination.straight import Straight
from services.straight import StraightService


class StraightEngine(Engine):
    def __init__(self):
        super().__init__(Straight)

    def get_discard_cards(self, card_in_hand, remaining_cards):
        best_low_value = self.get_best_low_value(card_in_hand, remaining_cards)
        best_straight = StraightService.next_5_values(best_low_value)
        duplicate_cards = self.duplicate_discard_cards(card_in_hand, best_straight)
        outside_cards = self.outside_cards(card_in_hand, best_straight)
        return duplicate_cards + outside_cards

    @staticmethod
    def outside_cards(card_in_hand, best_straight):
        return CardPile(
            [card for card in card_in_hand.cards if card.value not in best_straight]
        )

    # Get all the cards with duplicate_values
    @staticmethod
    def duplicate_discard_cards(card_in_hand, best_straight):
        discard_cards = CardPile([])
        for value in best_straight:
            number_of_cards = card_in_hand.number_of_card_with_value(value)
            if number_of_cards > 1:
                discard_cards += card_in_hand.get_cards_with_value(value).pick_cards(number_of_cards - 1)
        return discard_cards

    @classmethod
    def get_best_low_value(cls, card_in_hand, remaining_cards):
        straight_score = {}
        for value in cls.possible_values(card_in_hand, remaining_cards):
            straight_score[value] = cls.get_straight_score(card_in_hand, value)
        return max(straight_score, key=straight_score.get)

    @staticmethod
    def get_straight_score(card_in_hand, low_value):
        raise NotImplementedError

    @staticmethod
    def possible_values(card_in_hand, remaining_cards):
        raise NotImplementedError
