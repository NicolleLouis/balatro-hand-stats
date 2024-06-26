import pytest

from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.deck.base_deck import BaseDeck


def test_get_by_value():
    card_pile = BaseDeck().pile
    assert card_pile.number_of_card_with_value(2) == 4


def test_get_by_suit():
    card_pile = BaseDeck().pile
    assert card_pile.number_of_card_with_suit(Suit.SPADES) == 13


def test_equality():
    card = Card(Suit.SPADES, 2)
    pile_1 = CardPile({card})
    pile_2 = CardPile({card})
    assert pile_1 == pile_2


def test_non_equality():
    card = Card(Suit.SPADES, 2)
    lookalike = Card(Suit.SPADES, 2)
    pile_1 = CardPile({card})
    pile_2 = CardPile({lookalike})
    assert pile_1 != pile_2


def test_str_card_pile():
    card_pile = BaseDeck().pile
    assert str(card_pile) == "52 cards in pile"


def test_length():
    card_pile = BaseDeck().pile
    assert len(card_pile) == 52


def test_addition():
    card_pile = BaseDeck().pile
    card_pile_2 = BaseDeck().pile
    new_pile = card_pile + card_pile_2
    assert len(new_pile) == 104


def test_subtraction_complete_case():
    card = Card(Suit.SPADES, 2)
    card_pile = CardPile({card})
    card_pile_2 = CardPile({card})
    new_pile = card_pile - card_pile_2
    assert len(new_pile) == 0


def test_subtraction_with_non_existing_cards():
    card = Card(Suit.SPADES, 2)
    card_pile = CardPile()
    card_pile_2 = CardPile({card})
    new_pile = card_pile - card_pile_2
    assert len(new_pile) == 0


def test_subtraction_with_remaining_cards():
    card_1 = Card(Suit.SPADES, 2)
    card_2 = Card(Suit.SPADES, 2)
    card_pile = CardPile({card_1, card_2})
    card_pile_2 = CardPile({card_1})
    new_pile = card_pile - card_pile_2
    assert new_pile == CardPile({card_2})


def test_draw_cards():
    card_pile = BaseDeck().pile
    hand = card_pile.draw_cards(8)
    assert len(hand) == 8
    assert len(card_pile) == 44


def test_draw_too_many_cards():
    card_pile = BaseDeck().pile
    hand = card_pile.draw_cards(53)
    assert len(hand) == 52
    assert len(card_pile) == 0


def test_remove_card_pile():
    card = Card(Suit.SPADES, 2)
    lookalike = Card(Suit.SPADES, 2)
    card_pile = CardPile({card, lookalike})
    assert len(card_pile) == 2

    card_pile.remove_card_pile(CardPile({card}))
    assert len(card_pile) == 1


def test_remove_illegal_card():
    card = Card(Suit.SPADES, 2)
    lookalike = Card(Suit.SPADES, 2)
    card_pile = CardPile({card})

    card_pile.remove_card_pile(CardPile({lookalike}))
    assert card_pile == CardPile({card})


def test_pick_cards():
    card = Card(Suit.SPADES, 2)
    card_pile = CardPile({card})
    random_card = card_pile.pick_cards(1)
    assert len(random_card) == 1

    # Should not take card away from base pile
    assert len(card_pile) == 1


def test_pick_too_many_cards():
    card = Card(Suit.SPADES, 2)
    card_pile = CardPile({card})
    random_card = card_pile.pick_cards(10)

    # Should still take only 1 card
    assert len(random_card) == 1


def test_get_card_by_suit_single_card_case():
    card = Card(Suit.SPADES, 2)
    card_pile = CardPile({card})
    assert card_pile.get_cards_with_suit(Suit.SPADES) == card_pile
    assert card_pile.get_cards_with_suit(Suit.HEARTS) == CardPile()


def test_get_card_by_suit_multiple_cards_case():
    card = Card(Suit.SPADES, 2)
    target_pile = CardPile({card})
    card_pile = target_pile + CardPile({
        Card(Suit.CLUBS, 3),
        Card(Suit.CLUBS, 4),
        Card(Suit.CLUBS, 5),

    })
    assert card_pile.get_cards_with_suit(Suit.SPADES) == target_pile
    assert card_pile.get_cards_with_suit(Suit.HEARTS) == CardPile()


def test_get_distinct_values():
    card_pile = CardPile({
        Card(Suit.SPADES, 2),
        Card(Suit.CLUBS, 3),
        Card(Suit.CLUBS, 4),
        Card(Suit.CLUBS, 4),
    })
    assert card_pile.get_distinct_values() == {2, 3, 4}
