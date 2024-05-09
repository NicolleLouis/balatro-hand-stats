from __future__ import annotations


import random

from constants.suit import Suit
from models.card_pile import CardPile
from models.event.event import Event

"""
STC -> Suit-changing Tarot Card
"""


class STC(Event):
    def __init__(self, deck):
        super().__init__(deck)
        self.suit = self.random_suit()
        self.suit_repartition = self.deck.suit_repartition()

    # Draw 8 cards from the deck
    # Choose 3 cards at most from the 8
    # Change the suit of the chosen cards
    def perform(self) -> None:
        cards = self.deck.pile.pick_cards(8)
        target_suits = self.target_suit_order()
        cards_to_switch = self.pick_cards_to_switch(cards, target_suits)
        self.transform_cards(cards_to_switch)

    def transform_cards(self, cards_to_switch: CardPile) -> None:
        for card in cards_to_switch.cards:
            card.suit = self.suit

    @staticmethod
    def pick_cards_to_switch(cards: CardPile, target_suits) -> CardPile:
        cards_to_switch = CardPile()
        for suit in target_suits:
            if len(cards_to_switch) >= 3:
                break
            cards_to_switch += cards.get_cards_with_suit(suit)
        return cards_to_switch.pick_cards(3)

    # This ensures we don't work in reverse order by deleting cards from a better suit
    def legal_suits(self) -> list:
        legal_suits = [
            suit for suit in Suit.ALL_SUITS if self.suit_repartition[suit] <= self.suit_repartition[self.suit]
        ]
        return [suit for suit in legal_suits if suit != self.suit]

    # This will order the legal suits in ascending order of their repartition
    def target_suit_order(self) -> list:
        legal_suits = self.legal_suits()
        return sorted(legal_suits, key=lambda suit: self.suit_repartition[suit])

    @staticmethod
    def random_suit() -> str:
        return random.choice(Suit.ALL_SUITS)
