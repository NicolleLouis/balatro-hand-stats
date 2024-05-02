from models.card import Card


def test_str():
    jack_of_spade = Card('Spade', 11)
    assert str(jack_of_spade) == 'Jack of Spade'
