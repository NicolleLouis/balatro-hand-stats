from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from models.card_pile import CardPile

if TYPE_CHECKING:
    from models.deck.deck import Deck
    from models.engine.engine import Engine
    from models.event_setting import EventSetting
    from models.game_setting import GameSetting


class Game:
    def __init__(
            self,
            game_setting: GameSetting,
            deck: Deck,
            engine: Engine,
            event_setting: Optional[EventSetting] = None,
            visual: bool = False,
    ):
        self.deck: Deck = deck
        self.engine: Engine = engine
        self.game_setting: GameSetting = game_setting
        self.event_setting: Optional[EventSetting] = event_setting
        self.visual = visual

        self.hand_number: int = 0
        self.discard_number: int = 0
        self.draw_pile: CardPile = deck.pile
        self.discard_pile: CardPile = CardPile([])
        self.hand: CardPile = CardPile([])
        self.victory: bool = False

    def is_finished(self) -> bool:
        if self.engine.result(self.hand):
            self.victory = True
            return True

        if self.discard_number >= self.game_setting.discard_number:
            return True

        return False

    def run(self):
        self.initialize()

        while not self.is_finished():
            if self.visual:
                self.pretty_print()
            self.turn()

        if self.visual:
            self.pretty_print()
            print(f"Victory: {self.victory}")

    def initialize(self):
        self.draw_pile.shuffle()
        if self.event_setting:
            self.event_setting.perform(self.deck)
        self.draw()

    def turn(self):
        self.discard(self.engine.discard(self.hand, self.draw_pile))
        self.discard_number += 1
        self.draw()

    def draw(self):
        missing_cards_number = self.game_setting.card_in_hand_number - len(self.hand)
        self.hand += self.draw_pile.draw_cards(missing_cards_number)

    def discard(self, cards: CardPile):
        self.hand -= cards
        self.discard_pile += cards

    def pretty_print(self):
        print(f"Discard Number {self.discard_number}")
        print(f"Hand: ")
        self.hand.pretty_print()
        print("####################")
