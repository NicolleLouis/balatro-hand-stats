from models.deck_setting import DeckSetting
from models.decks.erratic import ErraticDeck
from models.engine.flush.flush_1 import FlushV1Engine
from models.engine.flush.flush_2 import FlushV2Engine
from models.game_setting import GameSetting
from models.probability_computer import ProbabilityComputer


deck = ErraticDeck
game_setting = GameSetting(1, 3, 8)
engine = FlushV2Engine()
deck_settings = DeckSetting(deck_size=19)

computer = ProbabilityComputer(deck, game_setting, engine, 100000, deck_settings)
computer.run()
