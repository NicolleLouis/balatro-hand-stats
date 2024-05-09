from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from services.straight import StraightService


def test_next_5_values_not_ace():
    assert StraightService.next_5_values(2) == [2, 3, 4, 5, 6]


def test_next_5_values_ace():
    assert StraightService.next_5_values(14) == [14, 2, 3, 4, 5]


def test_cards_in_suit_from_low_value():
    pile = CardPile([
        Card(Suit.SPADES, 2),
        Card(Suit.HEARTS, 2),
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 4),
        Card(Suit.CLUBS, 6),
        Card(Suit.CLUBS, 7),
        Card(Suit.CLUBS, 8),
    ])
    assert StraightService.cards_in_suit_from_low_value(pile, 2) == 3
