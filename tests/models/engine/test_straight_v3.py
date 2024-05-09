from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.engine.straight.straight_3 import StraightV3Engine


def test_should_take_6_ace_low_case():
    card_in_hands = CardPile({
        Card(Suit.HEARTS, 14),
        Card(Suit.DIAMONDS, 2),
        Card(Suit.DIAMONDS, 3),
        Card(Suit.SPADES, 4),
    })
    assert not StraightV3Engine.should_take_6(
        card_pile=card_in_hands,
        missing_values=[5],
        low_value=14
    )


def test_should_take_6_correct_case():
    card_in_hands = CardPile({
        Card(Suit.DIAMONDS, 2),
        Card(Suit.DIAMONDS, 3),
        Card(Suit.SPADES, 4),
        Card(Suit.HEARTS, 5),
    })
    assert StraightV3Engine.should_take_6(
        card_pile=card_in_hands,
        missing_values=[14],
        low_value=14
    )


def test_should_take_6_hole_case():
    card_in_hands = CardPile({
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 5),
        Card(Suit.SPADES, 7),
        Card(Suit.HEARTS, 8),
    })
    assert not StraightV3Engine.should_take_6(
        card_pile=card_in_hands,
        missing_values=[6],
        low_value=4
    )


def test_should_take_6_only_3_card_case():
    card_in_hands = CardPile({
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 5),
        Card(Suit.SPADES, 7),
    })
    assert not StraightV3Engine.should_take_6(
        card_pile=card_in_hands,
        missing_values=[6, 8],
        low_value=4
    )


def test_missing_values_case_hole():
    card_in_hands = CardPile({
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 5),
        Card(Suit.SPADES, 7),
        Card(Suit.HEARTS, 8),
    })
    missing_values = StraightV3Engine.missing_values(
        card_pile=card_in_hands,
        low_value=4
    )
    assert missing_values == [6]


def test_missing_values_case_only_3_cards():
    card_in_hands = CardPile({
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 5),
        Card(Suit.HEARTS, 6),
    })
    missing_values = StraightV3Engine.missing_values(
        card_pile=card_in_hands,
        low_value=2
    )
    assert missing_values == [2, 3]


def test_missing_values_case_ace_low():
    card_in_hands = CardPile({
        Card(Suit.DIAMONDS, 2),
        Card(Suit.DIAMONDS, 3),
        Card(Suit.HEARTS, 4),
        Card(Suit.HEARTS, 14),
    })
    missing_values = StraightV3Engine.missing_values(
        card_pile=card_in_hands,
        low_value=14
    )
    assert missing_values == [5]


def test_missing_values_case_4_consecutive():
    card_in_hands = CardPile({
        Card(Suit.DIAMONDS, 2),
        Card(Suit.DIAMONDS, 3),
        Card(Suit.HEARTS, 4),
        Card(Suit.HEARTS, 5),
    })
    missing_values = StraightV3Engine.missing_values(
        card_pile=card_in_hands,
        low_value=14
    )
    assert missing_values == [14, 6]


def test_outs_probability_case_hole():
    card_in_hands = CardPile({
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 5),
        Card(Suit.SPADES, 7),
        Card(Suit.HEARTS, 8),
    })
    remaining_cards = CardPile({
        Card(Suit.DIAMONDS, 6),
        Card(Suit.SPADES, 9),
    })
    outs_probability = StraightV3Engine.add_outs_probability(
        card_in_hand=card_in_hands,
        remaining_cards=remaining_cards,
        low_value=4
    )
    assert outs_probability == 0.5


def test_outs_probability_case_3_consecutive():
    card_in_hands = CardPile({
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 5),
        Card(Suit.SPADES, 6),
    })
    remaining_cards = CardPile({
        Card(Suit.DIAMONDS, 3),
        Card(Suit.SPADES, 7),
        Card(Suit.SPADES, 10),
        Card(Suit.SPADES, 10),
    })
    outs_probability = StraightV3Engine.add_outs_probability(
        card_in_hand=card_in_hands,
        remaining_cards=remaining_cards,
        low_value=3
    )
    assert outs_probability == 0.5


def test_score_case_3_consecutive():
    card_in_hands = CardPile({
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 5),
        Card(Suit.SPADES, 6),
    })
    remaining_cards = CardPile({
        Card(Suit.DIAMONDS, 3),
        Card(Suit.SPADES, 7),
        Card(Suit.SPADES, 10),
        Card(Suit.SPADES, 10),
    })
    score = StraightV3Engine.get_straight_score(
        card_in_hand=card_in_hands,
        remaining_cards=remaining_cards,
        low_value=3
    )
    assert score == 3.25


def test_score_case_hole():
    card_in_hands = CardPile({
        Card(Suit.DIAMONDS, 4),
        Card(Suit.DIAMONDS, 5),
        Card(Suit.SPADES, 6),
    })
    remaining_cards = CardPile({
        Card(Suit.DIAMONDS, 3),
        Card(Suit.SPADES, 7),
        Card(Suit.SPADES, 10),
        Card(Suit.SPADES, 10),
    })
    score = StraightV3Engine.get_straight_score(
        card_in_hand=card_in_hands,
        remaining_cards=remaining_cards,
        low_value=3
    )
    assert score == 3.25
