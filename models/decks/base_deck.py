from constants.suit import Suit
from models.card import Card
from models.decks.deck import Deck


class BaseDeck(Deck):
    def fill_deck(self):
        for value in range(2, 15):
            for suit in Suit.ALL_SUITS:
                self.cards.append(Card(suit, value))
