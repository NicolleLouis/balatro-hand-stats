from constants.suit import Suit
from models.card import Card
from models.decks.deck import Deck


class BaseDeck(Deck):
    def fill_deck(self):
        for value in range(1, 14):
            for suit in [
                Suit.SPADES,
                Suit.DIAMONDS,
                Suit.CLUBS,
                Suit.HEARTS
            ]:
                self.cards.append(Card(suit, value))
