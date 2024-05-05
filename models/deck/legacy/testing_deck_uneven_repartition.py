from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.deck.deck import Deck


class TestingDeckUnevenRepartition(Deck):
    def fill_deck(self):
        cards = []
        repartition = {
            Suit.SPADES: 20,
            Suit.CLUBS: 19,
            Suit.HEARTS: 7,
            Suit.DIAMONDS: 6
        }
        for suit, card_number in repartition.items():
            for _ in range(card_number):
                cards.append(Card(suit, 2))
        self.pile = CardPile(cards)
