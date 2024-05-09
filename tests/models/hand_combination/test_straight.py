from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.hand_combination.straight import Straight


def test_does_not_contain_suit():
    pile = CardPile([
        Card(Suit.SPADES, 2),
        Card(Suit.HEARTS, 4),
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 5),
        Card(Suit.CLUBS, 6),
    ])
    assert not Straight(pile).result()


def test_contain_suit_not_ace():
    pile = CardPile([
        Card(Suit.SPADES, 2),
        Card(Suit.HEARTS, 3),
        Card(Suit.DIAMONDS, 6),
        Card(Suit.DIAMONDS, 5),
        Card(Suit.CLUBS, 4),
    ])
    assert Straight(pile).result()


def test_contain_suit_ace():
    pile = CardPile([
        Card(Suit.SPADES, 2),
        Card(Suit.HEARTS, 3),
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 5),
        Card(Suit.CLUBS, 14),
    ])
    assert Straight(pile).result()
