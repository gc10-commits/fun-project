"""Unit tests for Stargarden events and state."""

from __future__ import annotations

import random

from stargarden.events import make_events
from stargarden.state import Player


def test_events_have_choices():
    events = make_events()
    assert events, "Expected at least one event"
    for event in events:
        assert len(event.choices) >= 2
        for choice in event.choices:
            assert callable(choice.resolve)


def test_player_adjust_clamps_values():
    player = Player(name="Test")
    player.adjust(hull=5, morale=5, fuel=5)
    assert player.hull == player.max_stat
    assert player.morale == player.max_stat
    assert player.fuel == player.max_stat

    player.adjust(hull=-50, morale=-50, fuel=-50)
    assert player.hull == 0
    assert player.morale == 0
    assert player.fuel == 0


def test_choice_resolution_changes_state():
    player = Player(name="Tester")
    events = make_events()
    event = events[0]
    initial = (player.hull, player.morale, player.fuel)
    message = event.choices[0].resolve(player, random.Random(42))
    assert isinstance(message, str)
    final = (player.hull, player.morale, player.fuel)
    assert final != initial
