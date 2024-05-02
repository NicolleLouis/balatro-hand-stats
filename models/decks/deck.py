from constants.suit import Suit


class Deck:
    def __init__(self):
        self.cards = []
        self.fill_deck()

    def fill_deck(self):
        raise NotImplementedError

    def card_by_value(self, value):
        matching_card = [card for card in self.cards if card.value == value]
        return len(matching_card)

    def card_by_suit(self, suit):
        matching_card = [card for card in self.cards if card.suit == suit]
        return len(matching_card)

    def __str__(self):
        return f"{len(self.cards)} cards in deck"

    def suit_repartition(self):
        return {
            Suit.SPADES: self.card_by_suit(Suit.SPADES),
            Suit.HEARTS: self.card_by_suit(Suit.HEARTS),
            Suit.DIAMONDS: self.card_by_suit(Suit.DIAMONDS),
            Suit.CLUBS: self.card_by_suit(Suit.CLUBS),
        }

    def value_repartition(self):
        value_repartition = {}
        for value in range(1, 14):
            value_repartition[value] = self.card_by_value(value)
        return value_repartition
