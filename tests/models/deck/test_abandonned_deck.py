from constants.suit import Suit
from models.deck.abandoned_deck import AbandonedDeck


def test_base_deck_creation():
    deck = AbandonedDeck()
    assert len(deck.pile) == 40
    assert str(deck) == "40 cards in deck"


def test_suit_repartition():
    deck = AbandonedDeck()
    expected_repartition = {
        Suit.SPADES: 10,
        Suit.CLUBS: 10,
        Suit.DIAMONDS: 10,
        Suit.HEARTS: 10,
    }
    assert expected_repartition == deck.suit_repartition()


def test_value_repartition():
    deck = AbandonedDeck()
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
        11: 0,
        12: 0,
        13: 0,
        14: 4,
    }
    assert expected_repartition == deck.value_repartition()
