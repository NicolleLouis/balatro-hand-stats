import time

from models.deck.abandoned_deck import AbandonedDeck
from models.deck.base_deck import BaseDeck
from models.deck.erratic import ErraticDeck
from models.engine.straight.straight_3 import StraightV3Engine
from models.game_setting import GameSetting
from models.probability_computer import ProbabilityComputer

game_setting = GameSetting(1, 3, 8)
engine = StraightV3Engine()
run_number = 10000
decks = [BaseDeck, AbandonedDeck, ErraticDeck]


for deck in decks:
    print(f"Deck: {deck.__name__}")
    computer = ProbabilityComputer(
        game_setting=game_setting,
        engine=engine,
        run_number=run_number,
        deck=deck,
    )

    start_time = time.time()
    computer.run()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
