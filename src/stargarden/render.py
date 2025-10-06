"""Rendering helpers for the Stargarden adventure."""

from __future__ import annotations

from .state import Player


def banner() -> str:
    return r"""
   _____ _                     _                       _
  / ____| |                   | |                     | |
 | (___ | |_ _ __ __ _  __ _  | |     ___   __ _  __ _| |_ ___  _ __
  \___ \| __| '__/ _` |/ _` | | |    / _ \ / _` |/ _` | __/ _ \| '__|
  ____) | |_| | | (_| | (_| | | |___| (_) | (_| | (_| | || (_) | |
 |_____/ \__|_|  \__,_|\__, | |______\___/ \__, |\__,_|\__\___/|_|
                        __/ |              __/ |
                       |___/              |___/
""".strip("\n")


def status_block(player: Player) -> str:
    return "\n".join(
        [
            _stat_line("Hull", player.hull, "🛠"),
            _stat_line("Morale", player.morale, "✨"),
            _stat_line("Fuel", player.fuel, "⛽"),
            f"Cargo: {', '.join(player.cargo) if player.cargo else '(empty)'}",
        ]
    )


def finale_message(player: Player) -> str:
    if player.is_stranded():
        return (
            "\nYour journey ends before the Aurora Rendezvous. "
            f"{player.failure_reason()}\n"
        )

    days = player.day - 1
    cargo = ", ".join(player.cargo) if player.cargo else "memories of the stars"
    return (
        "\nThe Aurora Rendezvous station shimmers ahead!\n"
        f"In {days} days you carried {cargo} across the cosmos.\n"
        "The crew of the Stargarden cheers your command.\n"
    )


def _stat_line(label: str, value: int, icon: str) -> str:
    filled = "█" * value
    empty = "·" * max(0, 12 - value)
    return f"{icon} {label:<6}: {filled}{empty} ({value})"
