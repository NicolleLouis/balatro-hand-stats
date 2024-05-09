import random

from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.deck.deck import Deck


class ErraticDeck(Deck):
    def fill_deck(self):
        cards = set()
        for _ in range(52):
            cards.add(self.generate_card())
        self.pile = CardPile(cards)

    @staticmethod
    def generate_card():
        value = random.choice(range(2, 15))
        suit = random.choice(Suit.ALL_SUITS)
        return Card(suit, value)
