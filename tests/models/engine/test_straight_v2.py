from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.deck.base_deck import BaseDeck
from models.engine.straight.straight_2 import StraightV2Engine


def test_get_straight_score():
    card_in_hand = CardPile({
        Card(Suit.HEARTS, 2),
        Card(Suit.SPADES, 3),
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 6),
        Card(Suit.SPADES, 11),
    })
    remaining_cards = CardPile()
    assert StraightV2Engine.get_straight_score(card_in_hand, remaining_cards, 2) == 3.5
    assert StraightV2Engine.get_straight_score(card_in_hand, remaining_cards, 10) == 1
    assert StraightV2Engine.get_straight_score(card_in_hand, remaining_cards, 14) == 3


def test_get_best_straight():
    card_in_hand = CardPile({
        Card(Suit.HEARTS, 2),
        Card(Suit.SPADES, 3),
        Card(Suit.HEARTS, 4),
        Card(Suit.DIAMONDS, 6),
        Card(Suit.HEARTS, 7),
        Card(Suit.CLUBS, 9),
        Card(Suit.DIAMONDS, 10),
        Card(Suit.SPADES, 14),
    })
    remaining_cards = BaseDeck().pile
    assert StraightV2Engine.get_best_low_value(card_in_hand, remaining_cards) in [2, 14]
