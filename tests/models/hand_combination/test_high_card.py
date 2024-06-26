from models.card_pile import CardPile
from models.deck.base_deck import BaseDeck
from models.hand_combination.high_card import HighCard


def test_successful_hand():
    card_pile = BaseDeck().pile
    assert HighCard(card_pile).result()


def test_empty_hand():
    card_pile = CardPile()
    assert not HighCard(card_pile).result()


def test_winning_hand():
    card_pile = BaseDeck().pile
    high_card = HighCard(card_pile)
    high_card.result()
    assert high_card.hand_description == "High Card: Ace"
