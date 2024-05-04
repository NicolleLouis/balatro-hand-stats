from models.deck_setting import DeckSetting
from models.decks.base_deck import BaseDeck
from models.decks.erratic import ErraticDeck
from models.engine.flush_0 import FlushV0Engine
from models.engine.flush_1 import FlushV1Engine
from models.game_setting import GameSetting
from models.probability_computer import ProbabilityComputer


deck = ErraticDeck
game_setting = GameSetting(1, 3, 8)
engine = FlushV0Engine()
deck_setting = DeckSetting(deck_size=19)

computer = ProbabilityComputer(deck, game_setting, engine, 100000, deck_setting)
computer.run()
