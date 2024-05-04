from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.decks.deck import Deck


# Base deck after an STC making it 16 spades and 12 of each other suit
# noinspection PyPep8Naming
class BaseDeck_16_12_12_12(Deck):
    def fill_deck(self):
        cards = []
        # Create all suited cards except Aces
        for value in range(2, 14):
            for suit in Suit.ALL_SUITS:
                cards.append(Card(suit, value))

        # Create all Aces as Spades
        for _ in range(4):
            cards.append(Card(Suit.SPADES, 14))

        self.pile = CardPile(cards)
