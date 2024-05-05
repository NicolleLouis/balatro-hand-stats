from models.deck.base_deck import BaseDeck
from models.engine.high_card import HighCardEngine
from models.game_setting import GameSetting
from models.probability_computer import ProbabilityComputer


def test_add_victory():
    deck = BaseDeck()
    game_setting = GameSetting(1, 1, 8)
    engine = HighCardEngine()
    computer = ProbabilityComputer(deck, game_setting, engine, 1)
    assert computer.victory_number == 0

    computer.add_victory(1)
    assert computer.victory_number == 1
    assert computer.victory_repartition == {1: 1}
