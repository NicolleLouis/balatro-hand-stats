from constants.suit import Suit
from models.deck_setting import DeckSetting
from models.deck.base_deck import BaseDeck


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


def test_deck_downsizing():
    deck_settings = DeckSetting(deck_size=3)
    deck = BaseDeck(deck_settings=deck_settings)
    assert len(deck.pile) == 3


# Random test, 1/52 to fail randomly, if it fails, relaunch to check
def test_deck_downsizing_randomness():
    deck_settings = DeckSetting(deck_size=1)
    deck_1 = BaseDeck(deck_settings=deck_settings)
    deck_2 = BaseDeck(deck_settings=deck_settings)
    card_1 = deck_1.pile.cards[0]
    card_2 = deck_2.pile.cards[0]
    assert card_1.value != card_2.value or card_1.suit != card_2.suit
