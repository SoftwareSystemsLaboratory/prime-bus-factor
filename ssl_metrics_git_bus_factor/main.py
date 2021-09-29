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

def buildBusFactorV2(commits: list) ->  DataFrame:
    maxDays: int = commits[-1]["day_since_0"]
    data: list = []

    day: int
    for day in range(maxDays + 1):
        data.append({})

    contributerCounter: int = 0
    currentDay: int = 0
    commit: dict
    for commit in commits:
        day: dict = commit["day_since_0"]

        if day != currentDay:
            currentDay = day
            contributerCounter = 0

        data[day][f"contributer_{contributerCounter}"] = commit["author_email"]
        data[day][f"contributer_{contributerCounter}_loc"] = abs(commit["delta_loc"])
        contributerCounter += 1

    return DataFrame(data)

def buildBusFactor(commits: list) -> list:
    data: list = []

    commit: dict
    for commit in commits:
        day: int = commit["day_since_0"]
        authorName: str = commit["author_name"]
        authorEmail: str = commit["author_email"]
        authorLOC: int = abs(commit["delta_loc"])

        dataRecord: dict = {
            "author_email": authorEmail,
            "author_name": authorName,
            "loc": authorLOC,
            "commits": 1,
            "day": day,
        }

        data.append(dataRecord)

    return data


def dumpJSON(json: Any, filename: str) -> None:
    with open(file=filename, mode="w") as file:
        dump(json, file)
        file.close()


def main() -> None:
    args: Namespace = get_argparse()

    if args.input[-5::] != ".json":
        print("Invalid input file type. Input file must be JSON")
        quit(1)

    data: list = loadJSON(filename=args.input)
    bf: dict = buildBusFactor(data)
    dumpJSON(bf, args.output)

    buildBusFactorV2(data)


if __name__ == "__main__":  # maxDataRecords: int = 0
    # for item in data:
    #     maxlen(item))

    # print(maxDataRecords)a

    main()
