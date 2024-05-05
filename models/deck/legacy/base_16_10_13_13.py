from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.deck.deck import Deck


# Base deck after an STC making it 16 spades, 10 clubs and the rest regular
# noinspection PyPep8Naming
class BaseDeck_16_10_13_13(Deck):
    def fill_deck(self):
        cards = []
        for value in range(2, 15):
            for suit in Suit.ALL_SUITS:
                cards.append(self.generate_card(suit, value))
        self.pile = CardPile(cards)

    @staticmethod
    def generate_card(suit, value):
        if suit == Suit.CLUBS and value < 5:
            return Card(Suit.SPADES, value)
        return Card(suit, value)
