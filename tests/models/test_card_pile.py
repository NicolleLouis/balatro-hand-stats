import pytest

from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.decks.base_deck import BaseDeck


def test_get_by_value():
    deck = BaseDeck()
    card_pile = CardPile(deck.cards)
    assert card_pile.card_by_value(2) == 4


def test_get_by_suit():
    deck = BaseDeck()
    card_pile = CardPile(deck.cards)
    assert card_pile.card_by_suit(Suit.SPADES) == 13


def test_equality():
    card = Card(Suit.SPADES, 2)
    pile_1 = CardPile([card])
    pile_2 = CardPile([card])
    assert pile_1 == pile_2


def test_non_equality():
    card = Card(Suit.SPADES, 2)
    lookalike = Card(Suit.SPADES, 2)
    pile_1 = CardPile([card])
    pile_2 = CardPile([lookalike])
    assert pile_1 != pile_2


def test_str_card_pile():
    deck = BaseDeck()
    card_pile = CardPile(deck.cards)
    assert str(card_pile) == "52 cards in pile"


def test_shuffle():
    """
    Warning this test may randomly fail,
    we are checking the order of the first 3 cards to ensure it doesn't happen much
    """
    deck = BaseDeck()
    card_pile = CardPile(deck.cards)
    initial_order = card_pile.cards[:3].copy()
    card_pile.shuffle()
    second_order = card_pile.cards[:3].copy()
    assert initial_order != second_order


def test_draw_cards():
    deck = BaseDeck()
    card_pile = CardPile(deck.cards)
    hand = card_pile.draw_cards(8)
    assert len(hand.cards) == 8
    assert len(card_pile.cards) == 44


def test_draw_too_many_cards():
    deck = BaseDeck()
    card_pile = CardPile(deck.cards)
    hand = card_pile.draw_cards(53)
    assert len(hand.cards) == 52
    assert len(card_pile.cards) == 0


def test_remove_card_pile():
    card = Card(Suit.SPADES, 2)
    lookalike = Card(Suit.SPADES, 2)
    card_pile = CardPile([card, lookalike])
    assert len(card_pile.cards) == 2

    card_pile.remove_card_pile(CardPile([card]))
    assert len(card_pile.cards) == 1


def test_remove_illegal_card():
    card = Card(Suit.SPADES, 2)
    lookalike = Card(Suit.SPADES, 2)
    card_pile = CardPile([card])

    with pytest.raises(ValueError):
        card_pile.remove_card_pile(CardPile([lookalike]))


def test_pick_cards():
    card = Card(Suit.SPADES, 2)
    card_pile = CardPile([card])
    random_card = card_pile.pick_cards(1)
    assert len(random_card.cards) == 1

    # Should not take card away from base pile
    assert len(card_pile.cards) == 1


def test_pick_too_many_cards():
    card = Card(Suit.SPADES, 2)
    card_pile = CardPile([card])
    random_card = card_pile.pick_cards(10)

    # Should still take only 1 card
    assert len(random_card.cards) == 1
