from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.decks.base_deck import BaseDeck
from models.engine.high_card import HighCardEngine


def test_result_positive():
    engine = HighCardEngine()
    assert engine.result(CardPile([Card(Suit.SPADES, 2)]))


def test_result_negative():
    engine = HighCardEngine()
    assert not engine.result(CardPile([]))


def test_discard():
    engine = HighCardEngine()
    card_pile = BaseDeck().pile
    discarded_pile = engine.discard(card_pile, card_pile)
    assert len(discarded_pile) == 0
