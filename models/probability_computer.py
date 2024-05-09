from __future__ import annotations
from multiprocessing import Pool, cpu_count

from typing import TYPE_CHECKING, Type, Optional

from models.game import Game

if TYPE_CHECKING:
    from models.deck.deck import Deck
    from models.deck_setting import DeckSetting
    from models.engine.engine import Engine
    from models.event_setting import EventSetting
    from models.game_setting import GameSetting


class ProbabilityComputer:
    def __init__(
            self,
            deck: Type[Deck],
            game_setting: GameSetting,
            engine: Engine,
            run_number: int,
            deck_setting: Optional[DeckSetting] = None,
            event_setting: Optional[EventSetting] = None,
    ):
        self.deck = deck
        self.game_setting = game_setting
        self.engine = engine
        self.run_number = run_number
        self.deck_setting = deck_setting
        self.event_setting = event_setting

        self.victory_number = 0
        self.victory_repartition = {}

    def run(self):
        with Pool(cpu_count()) as process_pool:
            results = process_pool.map(self.run_single_game, range(self.run_number))
            for result in results:
                if result:
                    self.add_victory(result)
        self.display_result()

    def run_single_game(self, _):
        game = Game(
            self.game_setting,
            self.deck(self.deck_setting),
            self.engine,
            self.event_setting,
        )
        game.run()
        if game.victory:
            return game.discard_number

    def display_result(self):
        print(f"Hand Probability: {self.probability(self.victory_number)}%")
        self.display_victory_repartition()

    def display_victory_repartition(self):
        total_victory = 0
        for discard_number in sorted(self.victory_repartition):
            total_victory += self.victory_repartition[discard_number]
            print(f"Discard Number: {discard_number} - Total Probability: {self.probability(total_victory)}%")

    def probability(self, number):
        return round(100 * number / self.run_number, 2)

    def add_victory(self, turn_number):
        self.victory_number += 1
        if turn_number not in self.victory_repartition:
            self.victory_repartition[turn_number] = 1
        else:
            self.victory_repartition[turn_number] += 1
