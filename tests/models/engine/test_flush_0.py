from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.engine.flush_0 import FlushV0Engine


def test_result_negative():
    engine = FlushV0Engine()

    assert not engine.result(CardPile([
        Card(Suit.SPADES, 2)
    ]))


def test_result_positive():
    engine = FlushV0Engine()
    cards = []
    for _ in range(1, 6):
        cards.append(Card(Suit.SPADES, 2))

    assert engine.result(CardPile(cards))


def test_discards_case_flush():
    engine = FlushV0Engine()
    cards = []
    for _ in range(1, 6):
        cards.append(Card(Suit.SPADES, 2))
    card_in_hand = CardPile(cards)

    assert engine.discard(card_in_hand, card_in_hand) == CardPile([])


def test_discard_regular_case():
    engine = FlushV0Engine()
    heart_card = Card(Suit.HEARTS, 2)
    card_in_hand = CardPile([
        Card(Suit.SPADES, 2),
        Card(Suit.SPADES, 2),
        heart_card,
    ])

    assert engine.discard(card_in_hand, card_in_hand) == CardPile([heart_card])


def test_discard_four_spades_case():
    engine = FlushV0Engine()
    cards = []
    for _ in range(1, 5):
        cards.append(Card(Suit.SPADES, 2))
    card_in_hand = CardPile(cards)

    assert engine.discard(card_in_hand, card_in_hand) == CardPile([])
    assert not engine.result(card_in_hand)
