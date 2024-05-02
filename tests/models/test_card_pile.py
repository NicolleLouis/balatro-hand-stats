from constants.suit import Suit
from models.card_pile import CardPile
from models.decks.base_deck import BaseDeck


def test_get_by_value():
    deck = BaseDeck()
    card_pile = CardPile(deck.cards)
    assert card_pile.card_by_value(1) == 4


def test_get_by_suit():
    deck = BaseDeck()
    card_pile = CardPile(deck.cards)
    assert card_pile.card_by_suit(Suit.SPADES) == 13


def test_str_card_pile():
    deck = BaseDeck()
    card_pile = CardPile(deck.cards)
    assert str(card_pile) == "52 remaining cards in pile"


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
    assert len(hand) == 8
    assert len(card_pile.cards) == 44


def test_draw_too_many_cards():
    deck = BaseDeck()
    card_pile = CardPile(deck.cards)
    hand = card_pile.draw_cards(53)
    assert len(hand) == 52
    assert len(card_pile.cards) == 0
