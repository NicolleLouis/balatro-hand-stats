from models.decks.erratic import ErraticDeck


def test_erratic_creation():
    deck = ErraticDeck()
    assert len(deck.pile) == 52
