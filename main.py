import time

from models.deck.abandoned_deck import AbandonedDeck
from models.deck.base_deck import BaseDeck
from models.deck.erratic import ErraticDeck
from models.engine.straight.straight_1 import StraightV1Engine
from models.game_setting import GameSetting
from models.probability_computer import ProbabilityComputer


game_setting = GameSetting(1, 3, 8)
engine = StraightV1Engine()
run_number = 100000

computer = ProbabilityComputer(
        game_setting=game_setting,
        engine=engine,
        run_number=run_number,
        deck=AbandonedDeck,
    )

start_time = time.time()
computer.run()
end_time = time.time()
print(f"Time used: {end_time - start_time}")