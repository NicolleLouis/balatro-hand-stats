from constants.suit import Suit
from models.decks.legacy.base_26_9_9_8 import BaseDeck_26_9_9_8


def test_suit_repartition():
    deck = BaseDeck_26_9_9_8()
    assert len(deck.pile) == 52
    assert deck.pile.card_by_suit(Suit.SPADES) == 26
    assert deck.pile.card_by_suit(Suit.HEARTS) == 9
    assert deck.pile.card_by_suit(Suit.DIAMONDS) == 9
    assert deck.pile.card_by_suit(Suit.CLUBS) == 8
