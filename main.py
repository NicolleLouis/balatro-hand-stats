from models.deck.legacy.base_26_0_13_13 import BaseDeck_26_0_13_13
from models.deck.legacy.base_26_9_9_8 import BaseDeck_26_9_9_8
from models.engine.flush.flush_2 import FlushV2Engine
from models.game_setting import GameSetting
from models.probability_computer import ProbabilityComputer


game_setting = GameSetting(1, 3, 8)
engine = FlushV2Engine()
run_number = 100

print("Case 26/9/9/8")
deck = BaseDeck_26_9_9_8
computer = ProbabilityComputer(deck, game_setting, engine, run_number)
computer.run()

print("##########")

print("Case 26/0/13/13")
deck = BaseDeck_26_0_13_13
computer = ProbabilityComputer(deck, game_setting, engine, run_number)
computer.run()
