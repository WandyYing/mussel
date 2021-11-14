"""Console script for mussel."""

import fire


def help():
    print("mussel")
    print("=" * len("mussel"))
    print("A universal interface automation framework")


def main():
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
