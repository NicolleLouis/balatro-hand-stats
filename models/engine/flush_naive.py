from __future__ import annotations

from constants.suit import Suit
from models.engine.engine import Engine
from models.hand_combination.flush import Flush
from models.card_pile import CardPile


class FlushNaive(Engine):
    def __init__(self):
        super().__init__(Flush)

    def choose_discard(self, card_in_hand: CardPile, remaining_cards: CardPile) -> CardPile:
        if self.result(card_in_hand):
            return CardPile([])

    @staticmethod
    def suit_with_most_cards_in_hand(card_in_hand: CardPile) -> str:
        card_by_suit = {}
        for suit in Suit.ALL_SUITS:
            card_by_suit[suit] = card_in_hand.card_by_suit(suit)

        return max(card_by_suit.items(), key=lambda suit: suit[1])[0]

    def get_wrong_suit_cards(self, card_in_hand: CardPile) -> CardPile:
        best_suit = self.suit_with_most_cards_in_hand(card_in_hand)
        other_cards = [card for card in card_in_hand.cards if card.suit != best_suit]
        return CardPile(other_cards)
