from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.engine.straight.straight_0 import StraightV0Engine


def test_get_best_straight():
    card_in_hand = CardPile({
        Card(Suit.HEARTS, 2),
        Card(Suit.SPADES, 3),
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 6),
        Card(Suit.SPADES, 11),
    })
    assert StraightV0Engine.get_best_low_value(card_in_hand, CardPile()) == 2


def test_get_straight_score():
    card_in_hand = CardPile({
        Card(Suit.HEARTS, 2),
        Card(Suit.SPADES, 3),
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 6),
        Card(Suit.SPADES, 11),
    })
    remaining_cards = CardPile()
    assert StraightV0Engine.get_straight_score(card_in_hand, remaining_cards, 2) == 4
    assert StraightV0Engine.get_straight_score(card_in_hand, remaining_cards, 10) == 1
    assert StraightV0Engine.get_straight_score(card_in_hand, remaining_cards, 14) == 3
