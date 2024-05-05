class Event:
    def __init__(self, deck):
        self.deck = deck

    def perform(self) -> None:
        raise NotImplementedError
