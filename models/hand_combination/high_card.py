from constants.value import Value
from models.hand_combination.hand_combination import HandCombination


class HighCard(HandCombination):
    def result(self):
        if self.has_at_least_a_card():
            self.hand_description = f"High Card: {self.get_highest_value()}"
            return True
        return False

    def has_at_least_a_card(self):
        return len(self.card_pile) > 0

    def get_highest_value(self):
        highest_card = max(self.card_pile.cards, key=lambda card: card.value)
        return Value.translate(highest_card.value)

    def __str__(self):
        return "High Card"
