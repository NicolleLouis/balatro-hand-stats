from constants.value import Value
from models.hand_combination.hand_combination import HandCombination
from services.straight import StraightService


class Straight(HandCombination):
    def result(self):
        for low_value in Value.ALL_STRAIGHT_LOW_VALUES:
            if StraightService.cards_in_suit_from_low_value(self.card_pile, low_value) == 5:
                self.hand_description = f"{low_value} Straight"
                return True
        return False

    def __str__(self):
        return "Straight"
