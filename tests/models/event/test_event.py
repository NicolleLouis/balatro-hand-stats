import pytest

from models.deck.base_deck import BaseDeck
from models.event.event import Event


def test_not_implemented():
    deck = BaseDeck()
    with pytest.raises(NotImplementedError):
        Event(deck).perform()
