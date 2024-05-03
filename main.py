from models.decks.base_deck import BaseDeck
from models.engine.flush_naive import FlushNaiveEngine
from models.game_setting import GameSetting
from models.probability_computer import ProbabilityComputer


deck = BaseDeck
game_setting = GameSetting(1, 3, 11)
engine = FlushNaiveEngine()

computer = ProbabilityComputer(deck, game_setting, engine, 10000)
computer.run()
