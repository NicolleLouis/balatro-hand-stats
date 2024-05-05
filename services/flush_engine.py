from __future__ import annotations

from typing import Optional, List

from constants.suit import Suit
from models.card_pile import CardPile


class FlushEngineService:
    @staticmethod
    def get_wrong_suit_cards(card_in_hand: CardPile, best_suit: Optional[str]) -> CardPile:
        other_cards = [card for card in card_in_hand.cards if card.suit != best_suit]
        return CardPile(other_cards)

    @staticmethod
    def get_legal_suit_with_most_cards_in_hand(
            card_in_hand: CardPile,
            legal_suits: Optional[List[str]] = None
    ) -> Optional[str]:
        if legal_suits is None:
            legal_suits = Suit.ALL_SUITS
        card_by_suit = {}
        for suit in legal_suits:
            card_by_suit[suit] = card_in_hand.number_of_card_with_suit(suit)
        try:
            return max(card_by_suit.items(), key=lambda suit: suit[1])[0]
        except ValueError:
            return None

    @staticmethod
    def get_legal_suits(card_in_hand: CardPile, draw_pile: CardPile) -> List[str]:
        legal_suits = []
        for suit in Suit.ALL_SUITS:
            if card_in_hand.number_of_card_with_suit(suit) + draw_pile.number_of_card_with_suit(suit) >= 5:
                legal_suits.append(suit)
        return legal_suits

    @staticmethod
    def score_suit(card_in_hand: CardPile, draw_pile: CardPile, suit: str) -> int:
        matching_cards_in_hand = card_in_hand.number_of_card_with_suit(suit)
        draw_pile_density = draw_pile.number_of_card_with_suit(suit) / len(draw_pile)
        number_of_drawn_cards = min(5, len(card_in_hand) - matching_cards_in_hand)
        score = matching_cards_in_hand + number_of_drawn_cards * draw_pile_density
        return score

    @staticmethod
    def get_best_suit(card_in_hand: CardPile, draw_pile: CardPile) -> Optional[str]:
        legal_suits = FlushEngineService.get_legal_suits(card_in_hand, draw_pile)
        scored_suit = {}
        for suit in legal_suits:
            scored_suit[suit] = FlushEngineService.score_suit(card_in_hand, draw_pile, suit)
        try:
            return max(scored_suit.items(), key=lambda suit: suit[1])[0]
        except ValueError:
            return None
