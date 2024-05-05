from constants.suit import Suit
from models.deck.legacy.base_26_0_13_13 import BaseDeck_26_0_13_13


def test_suit_repartition():
    deck = BaseDeck_26_0_13_13()
    assert len(deck.pile) == 52
    assert deck.pile.number_of_card_with_suit(Suit.SPADES) == 26
    assert deck.pile.number_of_card_with_suit(Suit.CLUBS) == 0
    assert deck.pile.number_of_card_with_suit(Suit.HEARTS) == 13
    assert deck.pile.number_of_card_with_suit(Suit.DIAMONDS) == 13
