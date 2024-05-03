from constants.value import Value
from models.hand_combination.hand_combination import HandCombination


class HighCard(HandCombination):
    def result(self):
        if self.has_at_least_a_card():
            self.hand_description = f"High Card: {self.get_highest_value()}"
            return True
        return False

    def has_at_least_a_card(self):
        return len(self.card_pile.cards) > 0

    def get_highest_value(self):
        self.card_pile.cards.sort(key=lambda card: card.value, reverse=True)
        return Value.translate(self.card_pile.cards[0].value)

    def __str__(self):
        return "High Card"
