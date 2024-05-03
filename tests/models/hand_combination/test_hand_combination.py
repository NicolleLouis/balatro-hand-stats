import pytest

from models.card_pile import CardPile
from models.decks.base_deck import BaseDeck
from models.hand_combination.hand_combination import HandCombination


def test_result_error():
    with pytest.raises(NotImplementedError):
        deck = BaseDeck()
        card_pile = CardPile(deck.cards)
        HandCombination(card_pile).result()
