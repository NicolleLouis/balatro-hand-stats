import random


class CardPile:
    def __init__(self, cards: list):
        self.cards = cards.copy()

    def __eq__(self, other):
        self_included_in_other = all(card in other.cards for card in self.cards)
        other_included_in_self = all(card in self.cards for card in other.cards)
        return self_included_in_other and other_included_in_self

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return f"{len(self)} cards in pile"

    def __add__(self, other):
        return CardPile(self.cards + other.cards)

    def __sub__(self, other):
        return CardPile([card for card in self.cards if card not in other.cards])

    def pretty_print(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def number_of_card_with_value(self, value):
        return sum(card.value == value for card in self.cards)

    def number_of_card_with_suit(self, suit):
        return sum(card.suit == suit for card in self.cards)

    def contains_at_least_a_value_card(self, value):
        return any(card.value == value for card in self.cards)

    def get_cards_with_suit(self, suit):
        return CardPile([card for card in self.cards if card.suit == suit])

    def get_cards_with_value(self, value):
        return CardPile([card for card in self.cards if card.value == value])

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
