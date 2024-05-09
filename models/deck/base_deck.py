from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.deck.deck import Deck


class BaseDeck(Deck):
    def fill_deck(self):
        cards = set()
        for value in range(2, 15):
            for suit in Suit.ALL_SUITS:
                cards.add(Card(suit, value))
        self.pile = CardPile(cards)
