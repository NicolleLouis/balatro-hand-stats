import random


class CardPile:
    def __init__(self, cards):
        self.cards = cards.copy()

    def __eq__(self, other):
        return self.cards == other.cards

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return f"{len(self)} cards in pile"

    def __add__(self, other):
        return CardPile(self.cards + other.cards)

    def __sub__(self, other):
        return CardPile([card for card in self.cards if card not in other.cards])

    def shuffle(self):
        random.shuffle(self.cards)

    def card_by_value(self, value):
        matching_card = [card for card in self.cards if card.value == value]
        return len(matching_card)

    def card_by_suit(self, suit):
        matching_card = [card for card in self.cards if card.suit == suit]
        return len(matching_card)

    def remove_card_pile(self, card_pile):
        for card in card_pile.cards:
            self.cards.remove(card)

    # This pick cards from the pile but doesn't remove them
    def pick_cards(self, card_number):
        self.shuffle()
        return CardPile(self.cards[:card_number])

    # This draw card from the pile, so it removes them
    def draw_cards(self, card_number):
        drawn_cards = self.cards[:card_number]
        del self.cards[:card_number]
        return CardPile(drawn_cards)
