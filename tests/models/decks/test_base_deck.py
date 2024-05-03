from constants.suit import Suit
from models.decks.base_deck import BaseDeck


def test_base_deck_creation():
    deck = BaseDeck()
    assert len(deck.pile) == 52
    assert str(deck) == "52 cards in deck"


def test_suit_repartition():
    deck = BaseDeck()
    expected_repartition = {
        Suit.SPADES: 13,
        Suit.CLUBS: 13,
        Suit.DIAMONDS: 13,
        Suit.HEARTS: 13,
    }
    assert expected_repartition == deck.suit_repartition()


def test_value_repartition():
    deck = BaseDeck()
    expected_repartition = {
        2: 4,
        3: 4,
        4: 4,
        5: 4,
        6: 4,
        7: 4,
        8: 4,
        9: 4,
        10: 4,
        11: 4,
        12: 4,
        13: 4,
        14: 4,
    }
    assert expected_repartition == deck.value_repartition()
