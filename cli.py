import argparse

parser = argparse.ArgumentParser(
    description="CLI for communicating with an LLM",
    formatter_class=argparse.RawTextHelpFormatter,
)

parser.add_argument(
    "--products", "-p",
    nargs="+",
    help="Accepts multiple product JSON objects"
)

namespace = parser.parse_args()
