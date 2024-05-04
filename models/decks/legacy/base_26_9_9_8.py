from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.decks.deck import Deck


# Base deck after progressively converting cards into Spades, trying to remain even
# noinspection PyPep8Naming
class BaseDeck_26_9_9_8(Deck):
    def fill_deck(self):
        cards = []
        for value in range(2, 15):
            for suit in Suit.ALL_SUITS:
                cards.append(self.generate_card(suit, value))
        self.pile = CardPile(cards)

    @staticmethod
    def generate_card(suit, value):
        if value < 10 or value == 10 and suit in [Suit.HEARTS, Suit.DIAMONDS]:
            return Card(suit, value)
        return Card(Suit.SPADES, value)
