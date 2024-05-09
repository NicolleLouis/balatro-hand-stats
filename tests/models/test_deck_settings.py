from constants.suit import Suit
from models.card import Card
from models.card_pile import CardPile
from models.deck_setting import DeckSetting


def test_adapt_size():
    deck_setting = DeckSetting(deck_size=1)
    card_pile = CardPile({
        Card(Suit.HEARTS, 2),
        Card(Suit.HEARTS, 2),
    })
    deck_setting.adapt_size(card_pile)
    assert len(card_pile) == 1
