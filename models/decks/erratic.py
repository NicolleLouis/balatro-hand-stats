import random

from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.decks.deck import Deck


class ErraticDeck(Deck):
    def fill_deck(self):
        cards = []
        for _ in range(52):
            cards.append(self.generate_card())
        self.pile = CardPile(cards)

    @staticmethod
    def generate_card():
        value = random.choice(range(2, 15))
        suit = random.choice(Suit.ALL_SUITS)
        return Card(suit, value)
