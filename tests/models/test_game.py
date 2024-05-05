from models.deck.base_deck import BaseDeck
from models.engine.high_card import HighCardEngine
from models.game import Game
from models.game_setting import GameSetting


def test_finished_victory():
    game_setting = GameSetting(1, 1, 8)
    deck = BaseDeck()
    engine = HighCardEngine()
    game = Game(game_setting, deck, engine)
    assert not game.victory
    assert not game.is_finished()

    game.hand = game.draw_pile.draw_cards(1)
    assert game.is_finished()
    assert game.victory


def test_finished_discard_number():
    game_setting = GameSetting(1, 1, 8)
    deck = BaseDeck()
    engine = HighCardEngine()
    game = Game(game_setting, deck, engine)
    assert not game.victory
    assert not game.is_finished()

    game.discard_number = 1
    assert game.is_finished()
    assert not game.victory


def test_draw_cards_from_empty_hand():
    game_setting = GameSetting(1, 1, 8)
    deck = BaseDeck()
    engine = HighCardEngine()
    game = Game(game_setting, deck, engine)
    assert len(game.hand) == 0

    game.draw()
    assert (len(game.hand) == 8)
    assert (len(game.draw_pile) == 44)


def test_draw_cards_from_non_empty_hand():
    game_setting = GameSetting(1, 1, 8)
    deck = BaseDeck()
    engine = HighCardEngine()
    game = Game(game_setting, deck, engine)
    game.hand = game.draw_pile.draw_cards(1)
    assert len(game.hand) == 1

    game.draw()
    assert (len(game.hand) == 8)
    assert (len(game.draw_pile) == 44)


def test_draw_cards_from_full_hand():
    game_setting = GameSetting(1, 1, 8)
    deck = BaseDeck()
    engine = HighCardEngine()
    game = Game(game_setting, deck, engine)
    game.hand = game.draw_pile.draw_cards(8)
    assert len(game.hand) == 8

    game.draw()
    assert (len(game.hand) == 8)
    assert (len(game.draw_pile) == 44)


def test_discard_hand():
    game_setting = GameSetting(1, 1, 8)
    deck = BaseDeck()
    engine = HighCardEngine()
    game = Game(game_setting, deck, engine)
    game.draw()
    assert len(game.hand) == 8

    game.discard(game.hand)
    assert len(game.hand) == 0
    assert len(game.discard_pile) == 8


def test_turn():
    game_setting = GameSetting(1, 1, 8)
    deck = BaseDeck()
    engine = HighCardEngine()
    game = Game(game_setting, deck, engine)
    game.draw()

    game.turn()
    assert len(game.hand) == 8
    assert len(game.discard_pile) == 0
    assert len(game.draw_pile) == 44
    assert game.discard_number == 1


def test_run():
    game_setting = GameSetting(1, 1, 8)
    deck = BaseDeck()
    engine = HighCardEngine()
    game = Game(game_setting, deck, engine)
    game.run()

    assert game.victory
    assert game.discard_number == 0
    assert len(game.hand) == 8
    assert len(game.discard_pile) == 0
    assert len(game.draw_pile) == 44
