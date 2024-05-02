from models.card import Card


class GameSetting:
    def __init__(
            self,
            hand_number: int,
            discard_number: int,
            card_in_hand_number: int,
            initial_deck: list[Card],
    ):
        self.hand_number = hand_number
        self.discard_number = discard_number
        self.card_in_hand_number = card_in_hand_number
        self.initial_deck = initial_deck
