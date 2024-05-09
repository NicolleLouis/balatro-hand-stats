from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.deck.base_deck import BaseDeck
from models.deck.erratic import ErraticDeck
from models.deck.legacy.testing_deck_uneven_repartition import TestingDeckUnevenRepartition
from models.event.stc import STC


def test_legal_suits_case_even():
    deck = BaseDeck()
    event = STC(deck)
    event.suit = Suit.SPADES
    assert sorted(event.legal_suits()) == sorted([Suit.CLUBS, Suit.HEARTS, Suit.DIAMONDS])


def test_legal_suits_case_uneven():
    deck = TestingDeckUnevenRepartition()
    event = STC(deck)
    event.suit = Suit.CLUBS
    assert sorted(event.legal_suits()) == sorted([Suit.DIAMONDS, Suit.HEARTS])


# Always at most 3 suits legally transformable since the bigger one will always be illegal
def test_legal_suits_case_erratic():
    deck = ErraticDeck()
    event = STC(deck)
    assert len(event.legal_suits()) <= 3


def test_target_suit_order():
    deck = TestingDeckUnevenRepartition()
    event = STC(deck)
    event.suit = Suit.SPADES
    assert event.target_suit_order() == [Suit.DIAMONDS, Suit.HEARTS, Suit.CLUBS]


def test_init():
    deck = BaseDeck()
    event = STC(deck)
    assert event.suit in Suit.ALL_SUITS


def test_pick_cards_to_switch_should_pick_at_most_3():
    deck = ErraticDeck()
    event = STC(deck)
    cards = deck.pile.pick_cards(8)
    target_suits = event.target_suit_order()
    cards_to_switch = event.pick_cards_to_switch(cards, target_suits)
    assert len(cards_to_switch) <= 3


def test_pick_cards_to_switch_should_pick_only_from_target_suits():
    deck = ErraticDeck()
    event = STC(deck)
    cards = deck.pile.pick_cards(8)
    target_suits = event.target_suit_order()
    cards_to_switch = event.pick_cards_to_switch(cards, target_suits)
    for card in cards_to_switch.cards:
        assert card.suit in target_suits


def test_pick_cards_to_switch_single_suit():
    event = STC(BaseDeck())
    club_pile = CardPile([
        Card(Suit.CLUBS, 2),
        Card(Suit.CLUBS, 3),
        Card(Suit.CLUBS, 4),
    ])
    cards = club_pile + CardPile([
        Card(Suit.SPADES, 2),
        Card(Suit.SPADES, 3),
        Card(Suit.SPADES, 4),
        Card(Suit.DIAMONDS, 8),
        Card(Suit.DIAMONDS, 9),

    ])
    target_suits = [Suit.CLUBS, Suit.DIAMONDS]
    cards_to_switch = event.pick_cards_to_switch(cards, target_suits)
    assert cards_to_switch == club_pile


def test_pick_cards_to_switch_multiple_suits():
    event = STC(BaseDeck())
    switch_cards = CardPile([
        Card(Suit.CLUBS, 2),
        Card(Suit.HEARTS, 3),
        Card(Suit.DIAMONDS, 4),
    ])
    cards = switch_cards + CardPile([
        Card(Suit.SPADES, 2),
        Card(Suit.SPADES, 3),
        Card(Suit.SPADES, 4),
        Card(Suit.SPADES, 8),
        Card(Suit.SPADES, 9),

    ])
    target_suits = [Suit.CLUBS, Suit.DIAMONDS, Suit.HEARTS]
    cards_to_switch = event.pick_cards_to_switch(cards, target_suits)
    assert cards_to_switch == switch_cards


def test_transform_cards():
    event = STC(BaseDeck())
    cards = CardPile([
        Card(Suit.CLUBS, 2),
        Card(Suit.HEARTS, 3),
        Card(Suit.DIAMONDS, 4),
    ])
    event.transform_cards(cards)
    for card in cards.cards:
        assert card.suit == event.suit


# Warning there is a small chance that this test fails randomly
# If the 8 drawn cards are all from the suit of the event. Which is quite improbable
def test_event_impact_deck():
    deck = BaseDeck()
    event = STC(deck)
    event.perform()

    assert len(deck.pile) == 52

    at_least_a_suit_changed = False

    for suit in Suit.ALL_SUITS:
        if deck.pile.number_of_card_with_suit(suit) != 13:
            at_least_a_suit_changed = True
            break

    assert at_least_a_suit_changed
