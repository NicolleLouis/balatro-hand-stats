import pytest

from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.engine.engine import Engine
from models.hand_combination.hand_combination import HandCombination
from models.hand_combination.high_card import HighCard


def test_discard():
    engine = Engine(HandCombination)

    with pytest.raises(NotImplementedError):
        engine.discard(CardPile([]), CardPile([]))


def test_result():
    engine = Engine(HighCard)

    assert engine.result(CardPile([
        Card(Suit.SPADES, 2)
    ]))
