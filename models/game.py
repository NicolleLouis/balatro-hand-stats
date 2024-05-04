from __future__ import annotations

from typing import TYPE_CHECKING

from models.card_pile import CardPile
from models.game_setting import GameSetting

if TYPE_CHECKING:
    from models.decks.deck import Deck
    from models.engine.engine import Engine


class Game:
    def __init__(
            self,
            game_setting: GameSetting,
            deck: Deck,
            engine: Engine,
    ):
        self.deck: Deck = deck
        self.engine: Engine = engine
        self.game_setting: GameSetting = game_setting

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
        self.draw_pile.shuffle()
        self.draw()

        while not self.is_finished():
            self.turn()

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
