from constants.suit import Suit
from models.deck.legacy.testing_deck_uneven_repartition import TestingDeckUnevenRepartition


def test_suit_repartition():
    deck = TestingDeckUnevenRepartition()
    assert len(deck.pile) == 52
    assert deck.pile.number_of_card_with_suit(Suit.SPADES) == 20
    assert deck.pile.number_of_card_with_suit(Suit.CLUBS) == 19
    assert deck.pile.number_of_card_with_suit(Suit.HEARTS) == 7
    assert deck.pile.number_of_card_with_suit(Suit.DIAMONDS) == 6
