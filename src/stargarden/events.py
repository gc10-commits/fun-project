"""Narrative events for the Stargarden adventure."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Callable, List

from .state import Player


OutcomeGenerator = Callable[[Player, random.Random], str]


@dataclass
class Choice:
    label: str
    resolve: OutcomeGenerator


@dataclass
class Event:
    name: str
    intro: str
    choices: List[Choice]


def make_events() -> List[Event]:
    """Create the reusable list of events."""

    return [
        _nebula_drift(),
        _stowaway_automaton(),
        _luminous_garden(),
        _quantum_markets(),
        _singing_meteor(),
        _wayward_signal(),
    ]


def _nebula_drift() -> Event:
    def manual(player: Player, rng: random.Random) -> str:
        player.adjust(fuel=-1)
        if rng.random() < 0.4:
            player.adjust(hull=-2)
            return (
                "The ship rattles as unseen rocks graze the hull. "
                "You steady the wheel and promise to recalibrate the sensors."
            )
        player.adjust(morale=1)
        return "Your daring navigation thrills the crew, and the nebula thins behind you."

    def drift(player: Player, rng: random.Random) -> str:
        player.adjust(morale=-1)
        player.adjust(fuel=1)
        if rng.random() < 0.5:
            player.add_cargo(["Nebula Bloom"])
            return (
                "You let the ship drift, gathering luminous spores that glow in the cargo bay."
            )
        return "Patience pays off as currents push you clear without further incident."

    return Event(
        name="Nebula Drift",
        intro=(
            "A rose-colored nebula envelopes the Stargarden. Turbulence jostles the hull and "
            "the guidance systems flicker."
        ),
        choices=[
            Choice("Navigate manually through the haze.", manual),
            Choice("Cut engines and drift with the currents.", drift),
        ],
    )


def _stowaway_automaton() -> Event:
    def recruit(player: Player, rng: random.Random) -> str:
        player.adjust(morale=2)
        if "Patchwork Automaton" not in player.cargo:
            player.add_cargo(["Patchwork Automaton"])
        return (
            "The automaton whirs happily, integrating with the crew and fixing dangling wires."
        )

    def trade(player: Player, rng: random.Random) -> str:
        player.adjust(fuel=2)
        player.adjust(morale=-1)
        return (
            "You broker a deal, trading the automaton to a merchant convoy for fuel cells."
        )

    return Event(
        name="Stowaway Automaton",
        intro=(
            "A tiny automaton rolls out from behind the hydroponics bay. Its eye-lights blink "
            "with hopeful rhythm."
        ),
        choices=[
            Choice("Offer the automaton a place on the crew.", recruit),
            Choice("Trade the automaton to the next convoy.", trade),
        ],
    )


def _luminous_garden() -> Event:
    def explore(player: Player, rng: random.Random) -> str:
        player.adjust(morale=2)
        if rng.random() < 0.3:
            player.adjust(hull=-1)
            return (
                "Bioluminescent vines curl around the ship, leaving scratches but filling the "
                "mess hall with gentle light."
            )
        player.add_cargo(["Starseed"])
        return "The crew returns with pockets full of starseeds that hum softly."

    def study(player: Player, rng: random.Random) -> str:
        player.adjust(fuel=1)
        player.adjust(morale=1)
        player.add_cargo(["Garden Samples"])
        return (
            "Scans reveal the garden's energy signatures. The data keeps the engines efficient "
            "for days."
        )

    return Event(
        name="Luminous Garden",
        intro=(
            "A rogue asteroid carries a thriving bioluminescent garden, beckoning with soft "
            "greens and blues."
        ),
        choices=[
            Choice("Send an away team to explore the garden.", explore),
            Choice("Study the garden from orbit and collect samples.", study),
        ],
    )


def _quantum_markets() -> Event:
    def barter(player: Player, rng: random.Random) -> str:
        if player.cargo:
            sold_item = rng.choice(player.cargo)
            player.remove_cargo([sold_item])
            player.adjust(fuel=2, morale=1)
            return f"You trade {sold_item} for a cache of fuel and energizing stories."
        player.adjust(fuel=1)
        return "Without anything to trade, a vendor slips you a sympathy ration of fuel."

    def perform(player: Player, rng: random.Random) -> str:
        player.adjust(morale=2)
        if rng.random() < 0.4:
            player.adjust(fuel=-1)
            return "The performance dazzles the crowd, but the celebration burns extra fuel."
        return "Your impromptu concert lifts spirits across the market promenade."

    return Event(
        name="Quantum Markets",
        intro=(
            "You dock with a wandering marketplace that flickers in and out of phase with "
            "reality."
        ),
        choices=[
            Choice("Barter with curious merchants.", barter),
            Choice("Perform a zero-gravity concert for tips.", perform),
        ],
    )


def _singing_meteor() -> Event:
    def chase(player: Player, rng: random.Random) -> str:
        player.adjust(fuel=-2)
        if rng.random() < 0.5:
            player.add_cargo(["Singing Meteor Shard"])
            player.adjust(morale=2)
            return "You capture a shard that harmonizes with the ship's engines."
        player.adjust(hull=-1)
        return "The meteor slips away, leaving only scorch marks to polish."

    def listen(player: Player, rng: random.Random) -> str:
        player.adjust(morale=1)
        return "The haunting melody guides your charts, revealing a shortcut through safe lanes."

    return Event(
        name="Singing Meteor",
        intro=(
            "Sensors detect a meteor trailing a trail of harmonics that resonate in the crew's "
            "bones."
        ),
        choices=[
            Choice("Chase the meteor and attempt capture.", chase),
            Choice("Record the melody and adjust your course.", listen),
        ],
    )


def _wayward_signal() -> Event:
    def decode(player: Player, rng: random.Random) -> str:
        player.adjust(morale=-1)
        player.adjust(fuel=1)
        return (
            "You spend the night decoding the signal—an ancient map that points toward the "
            "Aurora Rendezvous."
        )

    def reply(player: Player, rng: random.Random) -> str:
        player.adjust(morale=2)
        if rng.random() < 0.3:
            player.adjust(fuel=-2)
            return "The reply summons lost explorers who celebrate with you, but their tugs drain fuel."
        return "Your response echoes across the stars, and hopeful voices answer back."

    return Event(
        name="Wayward Signal",
        intro=(
            "A signal pings the comms array, repeating coordinates wrapped in forgotten dialects."
        ),
        choices=[
            Choice("Decode the signal into a proper star map.", decode),
            Choice("Reply and invite whoever sent it to meet you.", reply),
        ],
    )
