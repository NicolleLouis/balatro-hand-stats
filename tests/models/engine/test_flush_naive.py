from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.engine.flush_naive import FlushNaive


def test_result_negative():
    engine = FlushNaive()

    assert not engine.result(CardPile([
        Card(Suit.SPADES, 2)
    ]))


def test_result_positive():
    engine = FlushNaive()
    cards = []
    for _ in range(1, 6):
        cards.append(Card(Suit.SPADES, 2))

    assert engine.result(CardPile(cards))


def test_suit_with_most_cards_in_hand_simple():
    engine = FlushNaive()
    only_spades = CardPile([
        Card(Suit.SPADES, 2)
    ])
    assert engine.suit_with_most_cards_in_hand(only_spades) == Suit.SPADES


def test_suit_with_most_cards_in_hand():
    engine = FlushNaive()
    more_hearts = CardPile([
        Card(Suit.HEARTS, 2),
        Card(Suit.HEARTS, 2),
        Card(Suit.SPADES, 2),
        Card(Suit.DIAMONDS, 2),
        Card(Suit.CLUBS, 2),
    ])
    assert engine.suit_with_most_cards_in_hand(more_hearts) == Suit.HEARTS

def test_get_wrong_suit_cards():
    engine = FlushNaive()
    heart_1 = Card(Suit.HEARTS, 2)
    heart_2 = Card(Suit.HEARTS, 2)
    spade_1 = Card(Suit.SPADES, 2)
    card_in_hands = CardPile([
        heart_1,
        heart_2,
        spade_1
    ])
    expected_result = CardPile([spade_1])
    assert engine.get_wrong_suit_cards(card_in_hands) == expected_result
