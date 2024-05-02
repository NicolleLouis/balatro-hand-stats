import pytest

from constants.suit import Suit
from models.decks.base_deck import BaseDeck
from models.decks.deck import Deck


def test_abc_deck_creation():
    with pytest.raises(NotImplementedError):
        Deck()


def test_base_deck_creation():
    deck = BaseDeck()
    assert len(deck.cards) == 52
    assert str(deck) == "52 cards in deck"


def test_get_by_value():
    deck = BaseDeck()
    assert deck.card_by_value(1) == 4


def test_get_by_suit():
    deck = BaseDeck()
    assert deck.card_by_suit(Suit.SPADES) == 13
