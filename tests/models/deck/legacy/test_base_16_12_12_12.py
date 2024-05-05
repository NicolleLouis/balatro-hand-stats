from constants.suit import Suit
from models.deck.legacy.base_16_12_12_12 import BaseDeck_16_12_12_12


def test_suit_repartition():
    deck = BaseDeck_16_12_12_12()
    assert len(deck.pile) == 52
    assert deck.pile.number_of_card_with_suit(Suit.SPADES) == 16
    assert deck.pile.number_of_card_with_suit(Suit.HEARTS) == 12
    assert deck.pile.number_of_card_with_suit(Suit.DIAMONDS) == 12
    assert deck.pile.number_of_card_with_suit(Suit.CLUBS) == 12
