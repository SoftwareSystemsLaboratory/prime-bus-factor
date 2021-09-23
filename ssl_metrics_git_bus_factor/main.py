from json import dump, load
from typing import Any
from argparse import ArgumentParser, Namespace


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


def buildBusFactor(commits: list) -> dict:
    data: dict = {}

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
        }

        try:
            if type(data[day]) is list:
                HAS_RECORD: bool = False

                record: dict
                for record in data[day]:
                    if record["author_email"] == authorEmail:
                        record["loc"] += authorLOC
                        record["commits"] += 1
                        HAS_RECORD = True

                if HAS_RECORD == True:
                    pass
                else:
                    data[day].append(dataRecord)

        except KeyError:
            data[day] = []
            data[day].append(dataRecord)

    return data


def dumpJSON(json: Any, filename: str) -> None:
    with open(file=filename, mode="w") as file:
        dump(json, file)
        file.close()


def main() -> None:
    args: Namespace = get_argparse()
    data: list = loadJSON(filename=args.input)
    bf: dict = buildBusFactor(data)
    dumpJSON(bf, args.output)


if __name__ == "__main__":  # maxDataRecords: int = 0
    # for item in data:
    #     maxlen(item))

    # print(maxDataRecords)a

    main()
