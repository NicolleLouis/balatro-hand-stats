import time

from models.deck.base_deck import BaseDeck
from models.engine.straight import StraightEngine
from models.game_setting import GameSetting
from models.probability_computer import ProbabilityComputer


game_setting = GameSetting(1, 3, 8)
engine = StraightEngine()
run_number = 10000
computer = ProbabilityComputer(
        game_setting=game_setting,
        engine=engine,
        run_number=run_number,
        deck=BaseDeck,
    )

computer.run()
