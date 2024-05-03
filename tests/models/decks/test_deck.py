import pytest

from models.decks.deck import Deck


def test_abc_deck_creation():
    with pytest.raises(NotImplementedError):
        Deck()
