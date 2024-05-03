import random

from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.decks.base_deck import BaseDeck
from models.hand_combination.flush import Flush


def test_base_deck():
    card_pile = BaseDeck().pile
    assert Flush(card_pile).result()


def test_empty_hand():
    card_pile = CardPile([])
    assert not Flush(card_pile).result()


def test_closest_hand():
    cards = []
    for suite in Suit.ALL_SUITS:
        for value in range(2, 6):
            cards.append(Card(suit=suite, value=value))
    card_pile = CardPile(cards)
    assert not Flush(card_pile).result()


def test_winning_hand():
    suit = random.choice(Suit.ALL_SUITS)
    cards = []
    for _ in range(1, 6):
        cards.append(Card(suit=suit, value=random.choice(range(2, 15))))
    card_pile = CardPile(cards)
    flush = Flush(card_pile)
    flush.result()
    assert flush.hand_description == f"{suit} Flush"
