from constants.suit import Suit
from constants.value import Value
from models.card import Card
from models.card_pile import CardPile
from models.deck.abandoned_deck import AbandonedDeck
from models.deck.base_deck import BaseDeck
from services.straight import StraightService


def test_next_5_values_not_ace():
    assert StraightService.next_5_values(2) == [2, 3, 4, 5, 6]


def test_next_5_values_ace():
    assert StraightService.next_5_values(14) == [14, 2, 3, 4, 5]


def test_cards_in_suit_from_low_value():
    pile = CardPile({
        Card(Suit.SPADES, 2),
        Card(Suit.HEARTS, 2),
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 4),
        Card(Suit.CLUBS, 6),
        Card(Suit.CLUBS, 7),
        Card(Suit.CLUBS, 8),
    })
    assert StraightService.cards_in_suit_from_low_value(pile, 2) == 3


def test_get_legal_low_values_case_base_deck():
    all_cards = BaseDeck().pile
    assert StraightService.get_legal_low_values(all_cards) == Value.ALL_STRAIGHT_LOW_VALUES


def test_get_legal_low_values_case_abandoned_deck():
    all_cards = AbandonedDeck().pile
    expected_values = [14, 2, 3, 4, 5, 6]
    assert sorted(StraightService.get_legal_low_values(all_cards)) == sorted(expected_values)


def test_get_legal_low_values_case_custom_selection():
    all_cards = CardPile({
        Card(Suit.DIAMONDS, 14),
        Card(Suit.HEARTS, 2),
        Card(Suit.SPADES, 3),
        Card(Suit.SPADES, 4),
        Card(Suit.CLUBS, 5),
        Card(Suit.CLUBS, 7),
        Card(Suit.HEARTS, 9),
    })
    assert StraightService.get_legal_low_values(all_cards) == [14]


def test_holes_case_false():
    card_pile = CardPile({
        Card(Suit.DIAMONDS, 14),
        Card(Suit.HEARTS, 2),
        Card(Suit.SPADES, 4),
        Card(Suit.CLUBS, 5),
        Card(Suit.CLUBS, 7),
        Card(Suit.HEARTS, 9),
    })
    assert StraightService.has_holes(card_pile, 14)


def test_holes_case_true():
    card_pile = CardPile({
        Card(Suit.DIAMONDS, 14),
        Card(Suit.HEARTS, 2),
        Card(Suit.SPADES, 3),
        Card(Suit.CLUBS, 6),
        Card(Suit.CLUBS, 7),
        Card(Suit.HEARTS, 9),
    })
    assert not StraightService.has_holes(card_pile, 14)
