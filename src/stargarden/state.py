"""Game state data structures for Stargarden."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List


@dataclass
class Player:
    """Represents the captain and their ship."""

    name: str
    hull: int = 10
    morale: int = 10
    fuel: int = 10
    cargo: List[str] = field(default_factory=list)
    day: int = 1

    max_stat: int = 12

    def adjust(self, *, hull: int = 0, morale: int = 0, fuel: int = 0) -> None:
        """Apply stat changes while clamping to sensible limits."""

        self.hull = self._clamp(self.hull + hull)
        self.morale = self._clamp(self.morale + morale)
        self.fuel = self._clamp(self.fuel + fuel)

    def add_cargo(self, items: Iterable[str]) -> None:
        for item in items:
            if item not in self.cargo:
                self.cargo.append(item)

    def remove_cargo(self, items: Iterable[str]) -> None:
        to_remove = set(items)
        self.cargo = [item for item in self.cargo if item not in to_remove]

    def advance_day(self) -> None:
        self.day += 1

    def is_stranded(self) -> bool:
        return self.hull <= 0 or self.morale <= 0 or self.fuel <= 0

    def failure_reason(self) -> str:
        if self.hull <= 0:
            return "Your hull gave out under cosmic pressure."
        if self.morale <= 0:
            return "The crew's spirit faded into the nebula."
        if self.fuel <= 0:
            return "You drift endlessly with empty tanks."
        return "You vanished into deep space."  # fallback

    def status_summary(self) -> str:
        cargo_text = ", ".join(self.cargo) if self.cargo else "(empty)"
        return (
            f"Hull: {self.hull} | Morale: {self.morale} | Fuel: {self.fuel} | "
            f"Cargo: {cargo_text}"
        )

    def _clamp(self, value: int) -> int:
        return max(0, min(self.max_stat, value))
