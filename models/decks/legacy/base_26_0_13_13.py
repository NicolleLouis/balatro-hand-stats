from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.decks.deck import Deck


# Base deck, but we deleted the Clubs and made them Spades
# noinspection PyPep8Naming
class BaseDeck_26_0_13_13(Deck):
    def fill_deck(self):
        cards = []
        for value in range(2, 15):
            for suit in Suit.ALL_SUITS:
                cards.append(self.generate_card(suit, value))
        self.pile = CardPile(cards)

    @staticmethod
    def generate_card(suit, value):
        if suit == Suit.CLUBS:
            return Card(Suit.SPADES, value)
        return Card(suit, value)
