import pytest

from models.decks.base_deck import BaseDeck
from models.hand_combination.hand_combination import HandCombination


def test_result_error():
    with pytest.raises(NotImplementedError):
        HandCombination(BaseDeck().pile).result()
