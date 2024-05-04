from constants.suit import Suit
from models.decks.legacy.base_16_12_12_12 import BaseDeck_16_12_12_12


def test_suit_repartition():
    deck = BaseDeck_16_12_12_12()
    assert len(deck.pile) == 52
    assert deck.pile.card_by_suit(Suit.SPADES) == 16
    assert deck.pile.card_by_suit(Suit.HEARTS) == 12
    assert deck.pile.card_by_suit(Suit.DIAMONDS) == 12
    assert deck.pile.card_by_suit(Suit.CLUBS) == 12
