import pytest

from models.deck.deck import Deck


def test_abc_deck_creation():
    with pytest.raises(NotImplementedError):
        Deck()
