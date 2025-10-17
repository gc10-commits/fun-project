import argparse

"""Entry point for playing Stargarden."""

from stargarden import run_game


def main():
    parser = argparse.ArgumentParser(...)
    parser.add_argument(--resume, action='store_file', help="Resume previous progress from the given save file.", default='save.json')
    parser.add_argument(--seed, type=int, default=None, help="Seed for the random NVS generator")
    args = parser.parse_args()

    run_game(seed=args.seed, resume=args.resume)

if __name__ == "__main__":
    main()
