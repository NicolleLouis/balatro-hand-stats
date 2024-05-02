from constants.suit import Suit
from models.card_pile import CardPile


class Deck:
    def __init__(self):
        self.cards = []
        self.fill_deck()
        self.pile = CardPile(self.cards)

    def fill_deck(self):
        raise NotImplementedError

    def __str__(self):
        return f"{len(self.cards)} cards in deck"

    def suit_repartition(self):
        return {
            Suit.SPADES: self.pile.card_by_suit(Suit.SPADES),
            Suit.HEARTS: self.pile.card_by_suit(Suit.HEARTS),
            Suit.DIAMONDS: self.pile.card_by_suit(Suit.DIAMONDS),
            Suit.CLUBS: self.pile.card_by_suit(Suit.CLUBS),
        }

    def value_repartition(self):
        value_repartition = {}
        for value in range(1, 14):
            value_repartition[value] = self.pile.card_by_value(value)
        return value_repartition
