from models.deck.base_deck import BaseDeck
from models.engine.flush.flush_2 import FlushV2Engine
from models.event.stc import STC
from models.event_setting import EventSetting
from models.game_setting import GameSetting
from models.probability_computer import ProbabilityComputer


game_setting = GameSetting(1, 3, 8)
engine = FlushV2Engine()
run_number = 100000
events = []
event_setting = EventSetting(events)

for stc_used in range(26):
    print(f"STC used: {stc_used}")
    computer = ProbabilityComputer(
        game_setting=game_setting,
        engine=engine,
        run_number=run_number,
        event_setting=event_setting,
        deck=BaseDeck,
    )
    computer.run()
    event_setting.add_event(STC)
