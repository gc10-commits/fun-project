"""Interactive game loop for Stargarden."""

from __future__ import annotations

import random

from .events import Event, make_events
from .render import banner, finale_message, status_block
from .state import Player


def run_game(*, seed: int | None = None) -> None:
    """Launch the Stargarden adventure in the console."""

    rng = random.Random(seed)
    events = make_events()

    print(banner())
    print("\nWelcome to Stargarden, a pocket-sized spacefaring tale!\n")

    name = input("Captain, what is your name? ").strip() or "Nova"
    player = Player(name=name)

    print(
        "\nYour mission: guide the Stargarden to the Aurora Rendezvous before the seventh sunrise."
    )

    while not player.is_stranded() and player.day <= 7:
        print("\n" + "═" * 72)
        print(f"Day {player.day}: {player.name}, the crew awaits your decision.")

        event = rng.choice(events)
        _present_event(event, rng, player)

        if player.is_stranded():
            break

        player.advance_day()

    print(finale_message(player))


def _present_event(event: Event, rng: random.Random, player: Player) -> None:
    print(f"\n{event.name}\n{'-' * len(event.name)}")
    print(event.intro)

    print("\nChoices:")
    for index, choice in enumerate(event.choices, start=1):
        print(f"  {index}. {choice.label}")

    selection = _prompt_choice(len(event.choices))
    choice = event.choices[selection - 1]

    outcome = choice.resolve(player, rng)
    print(f"\n{outcome}\n")
    print(status_block(player))


def _prompt_choice(number_of_choices: int) -> int:
    while True:
        raw = input("\nYour decision (enter the number): ").strip()
        if not raw.isdigit():
            print("Please enter the number of the choice you wish to make.")
            continue
        value = int(raw)
        if 1 <= value <= number_of_choices:
            return value
        print(f"Choose a number between 1 and {number_of_choices}.")
