from argparse import ArgumentParser, Namespace
from json import dump, load
from typing import Any

from pandas.core.frame import DataFrame


def get_argparse() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="SSL Metrics - Bus Factor Calculator",
        usage="Takes a JSON file of commits as an input and returns the bus factor of commits for each day that the project exists.",
    )
    parser.add_argument(
        "-i",
        "--input",
        help="The input JSON file that is to be used for calculating the bus factor",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="The bus factor output JSON",
        type=str,
        required=True,
    )
    return parser.parse_args()

def loadJSON(filename: str) -> list:
    with open(file=filename, mode="r") as file:
        return load(file)


def buildBusFactor(commits: list) -> DataFrame:
    maxDays: int = commits[-1]["day_since_0"]
    data: list = []

    for commit in commits:
        temp: dict = {}
        temp["day"] = commit["day_since_0"]
        temp["contributor_count"] = #TODO: FINISH ME! 
        data.append(temp)

    return DataFrame(data)


def main() -> None:
    args: Namespace = get_argparse()

    if args.input[-5::] != ".json":
        print("Invalid input file type. Input file must be JSON")
        quit(1)

    data: list = loadJSON(filename=args.input)
    df: DataFrame = buildBusFactor(commits=data)
    df.to_json(args.output)


if __name__ == "__main__":  # maxDataRecords: int = 0
    main()
