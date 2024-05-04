from __future__ import annotations
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.card_pile import CardPile


class DeckSetting:
    def __init__(
            self,
            deck_size: Optional[int] = None
    ):
        self.deck_size = deck_size

    def perform(self, card_pile: CardPile) -> None:
        self.adapt_size(card_pile)

    def adapt_size(self, card_pile: CardPile) -> None:
        if self.deck_size is not None:
            card_pile.shuffle()
            card_pile.draw_cards(len(card_pile) - self.deck_size)
