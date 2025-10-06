# Stargarden

Stargarden is a pocket-sized narrative adventure that lives in your terminal. Each
in-game day, a new cosmic event challenges your crew. Balance hull integrity,
crew morale, and fuel reserves as you chart a course toward the mythical Aurora
Rendezvous station.

## Features

- **Choice-driven storytelling** – respond to colorful sci-fi events with unique
  outcomes that shape your ship and crew.
- **Dynamic status tracking** – hull, morale, and fuel respond immediately to
your decisions, keeping each run tense and replayable.
- **Collectible curiosities** – gather strange cargo like Nebula Blooms and
  Singing Meteor Shards to bring back to the rendezvous.

## Getting Started

This project targets Python 3.10 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

You can run the adventure directly with:

```bash
python main.py
```

Alternatively, import the package and start the game manually:

```python
from stargarden import run_game

run_game()
```

## Running Tests

The project includes lightweight unit tests for core mechanics. Execute them
with:

```bash
python -m pytest
```

## License

This project is released into the public domain under the [Unlicense](LICENSE).
