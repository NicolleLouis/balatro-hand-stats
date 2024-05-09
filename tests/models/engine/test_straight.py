from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.engine.straight.straight import StraightEngine


def test_duplicate_cards_case_no_duplicate():
    card_in_hand = CardPile({
        Card(Suit.HEARTS, 2),
        Card(Suit.SPADES, 3),
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 6),
        Card(Suit.SPADES, 11),
    })
    assert StraightEngine.duplicate_discard_cards(card_in_hand, [2, 3, 4, 5, 6]) == CardPile()


def test_duplicate_cards_case_duplicate():
    card_in_hand = CardPile({
        Card(Suit.HEARTS, 2),
        Card(Suit.SPADES, 2),
        Card(Suit.DIAMONDS, 8),
        Card(Suit.DIAMONDS, 8),
        Card(Suit.SPADES, 11),
    })
    duplicate_cards = StraightEngine.duplicate_discard_cards(card_in_hand, [2, 3, 4, 5, 6])
    assert duplicate_cards.number_of_card_with_value(2) == 1
    assert duplicate_cards.number_of_card_with_value(3) == 0
    assert duplicate_cards.number_of_card_with_value(4) == 0
    assert duplicate_cards.number_of_card_with_value(5) == 0
    assert duplicate_cards.number_of_card_with_value(6) == 0


def test_outside_cards():
    card_in_hand = CardPile({
        Card(Suit.HEARTS, 2),
        Card(Suit.SPADES, 2),
        Card(Suit.DIAMONDS, 8),
        Card(Suit.DIAMONDS, 8),
        Card(Suit.SPADES, 11),
    })
    duplicate_cards = StraightEngine.outside_cards(card_in_hand, [2, 3, 4, 5, 6])
    assert duplicate_cards.number_of_card_with_value(2) == 0
    assert duplicate_cards.number_of_card_with_value(8) == 2
    assert duplicate_cards.number_of_card_with_value(11) == 1
