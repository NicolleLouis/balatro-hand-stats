from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

if TYPE_CHECKING:
    from models.deck.deck import Deck
    from models.event.event import Event


class EventSetting:
    def __init__(
            self,
            events: Optional[list[Type[Event]]] = None,
    ):
        self.events = events if events else []

    def add_events(self, events: list[Type[Event]]) -> None:
        self.events.extend(events)

    def add_event(self, event: Type[Event]) -> None:
        self.events.append(event)

    def perform(self, deck: Deck) -> None:
        for event in self.events:
            event(deck).perform()
            deck.pile.shuffle()
