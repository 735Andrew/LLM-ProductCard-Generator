import argparse
import sys

parser = argparse.ArgumentParser(
    description="Takes set of products",
    formatter_class=argparse.RawTextHelpFormatter,
)

parser.add_argument(
    "--products",
    "-p",
    nargs=1,
    default={},
    help="Expects set of products."
)

namespace = parser.parse_args(sys.argv[1:])
