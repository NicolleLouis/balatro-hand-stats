from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.deck.base_deck import BaseDeck
from services.flush_engine import FlushEngineService


def test_suit_with_most_cards_in_hand_simple():
    only_spades = CardPile({
        Card(Suit.SPADES, 2)
    })
    assert FlushEngineService.get_legal_suit_with_most_cards_in_hand(only_spades) == Suit.SPADES


def test_suit_with_most_cards_in_hand():
    more_hearts = CardPile({
        Card(Suit.HEARTS, 2),
        Card(Suit.HEARTS, 2),
        Card(Suit.SPADES, 2),
        Card(Suit.DIAMONDS, 2),
        Card(Suit.CLUBS, 2),
    })
    assert FlushEngineService.get_legal_suit_with_most_cards_in_hand(more_hearts) == Suit.HEARTS


def test_get_wrong_suit_cards():
    heart_1 = Card(Suit.HEARTS, 2)
    heart_2 = Card(Suit.HEARTS, 2)
    spade_1 = Card(Suit.SPADES, 2)
    cards_in_hand = CardPile({
        heart_1,
        heart_2,
        spade_1
    })
    expected_result = CardPile({spade_1})
    assert FlushEngineService.get_wrong_suit_cards(cards_in_hand, Suit.HEARTS) == expected_result


def test_get_legal_suits_empty_piles():
    cards_in_hand = CardPile()
    draw_pile = CardPile()
    assert FlushEngineService.get_legal_suits(cards_in_hand, draw_pile) == []


def test_get_legal_suits_base_deck():
    deck = BaseDeck()
    draw_pile = deck.pile
    cards_in_hand = CardPile()
    assert FlushEngineService.get_legal_suits(cards_in_hand, draw_pile) == Suit.ALL_SUITS


def test_get_legal_suits_just_enough():
    cards_in_hand = CardPile({
        Card(Suit.SPADES, 2),
        Card(Suit.SPADES, 2),
        Card(Suit.SPADES, 2),
    })
    draw_pile = CardPile({
        Card(Suit.SPADES, 2),
        Card(Suit.SPADES, 2),
    })
    assert FlushEngineService.get_legal_suits(cards_in_hand, draw_pile) == [Suit.SPADES]


# Should discard the heart hoping for the spade, so discarding 1 card and EV is 1/2
def test_suit_scoring():
    cards_in_hand = CardPile({
        Card(Suit.SPADES, 2),
        Card(Suit.HEARTS, 2),
    })
    draw_pile = CardPile({
        Card(Suit.SPADES, 2),
        Card(Suit.HEARTS, 2),
    })
    assert FlushEngineService.score_suit(cards_in_hand, draw_pile, Suit.SPADES) == 3 / 2


def test_best_suit_no_legal_answer():
    cards_in_hand = CardPile({
        Card(Suit.SPADES, 2),
        Card(Suit.HEARTS, 2),
    })
    draw_pile = CardPile({
        Card(Suit.SPADES, 2),
        Card(Suit.HEARTS, 2),
        Card(Suit.HEARTS, 2),
    })
    assert FlushEngineService.get_best_suit(cards_in_hand, draw_pile) is None


def test_best_suit_iso_density():
    draw_pile = BaseDeck().pile
    cards_in_hand = CardPile({
        Card(Suit.SPADES, 2),
        Card(Suit.HEARTS, 2),
        Card(Suit.HEARTS, 2),
    })
    assert FlushEngineService.get_best_suit(cards_in_hand, draw_pile) == Suit.HEARTS


def test_best_suit_iso_hand():
    cards_in_hand = BaseDeck().pile
    draw_pile = CardPile({
        Card(Suit.SPADES, 2),
        Card(Suit.SPADES, 2),
        Card(Suit.HEARTS, 2),
    })
    assert FlushEngineService.get_best_suit(cards_in_hand, draw_pile) == Suit.SPADES


# Mode hearts in hand, but the spades are more likely to come
def test_best_suit_unintuitive():
    cards_in_hand = CardPile({
        Card(Suit.SPADES, 2),
        Card(Suit.SPADES, 2),
        Card(Suit.HEARTS, 2),
        Card(Suit.HEARTS, 2),
        Card(Suit.HEARTS, 2),
    })
    cards = set()
    for _ in range(5):
        cards.add(Card(Suit.SPADES, 2))
        cards.add(Card(Suit.SPADES, 2))
        cards.add(Card(Suit.HEARTS, 2))
    draw_pile = CardPile(cards)
    assert FlushEngineService.get_best_suit(cards_in_hand, draw_pile) == Suit.SPADES
