from __future__ import annotations

from typing import TYPE_CHECKING, Type, Optional

from models.game import Game

if TYPE_CHECKING:
    from models.deck.deck import Deck
    from models.engine.engine import Engine
    from models.game_setting import GameSetting
    from models.deck_setting import DeckSetting


class ProbabilityComputer:
    def __init__(
            self,
            deck: Type[Deck],
            game_setting: GameSetting,
            engine: Engine,
            run_number: int,
            deck_setting: Optional[DeckSetting] = None,
    ):
        self.deck = deck
        self.game_setting = game_setting
        self.engine = engine
        self.run_number = run_number
        self.victory_number = 0
        self.victory_repartition = {}
        self.deck_setting = deck_setting

    def run(self):
        for _ in range(self.run_number):
            game = Game(self.game_setting, self.deck(self.deck_setting), self.engine)
            game.run()
            if game.victory:
                self.add_victory(game.discard_number)
        self.display_result()

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