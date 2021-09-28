from argparse import ArgumentParser, Namespace
from typing import Any

import matplotlib.pyplot as plt
import pandas
from matplotlib.figure import Figure
from pandas import DataFrame


def get_argparse() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="SSL Metrics - Bus Factor Graph Creator",
        usage="Takes a JSON file of bus factor information as an input and outputs graphs based on the bus factor information.",
    )
    parser.add_argument(
        "-i",
        "--input",
        help="The input JSON file that is to be used for graphing",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="The output filename that is to be used for the graph",
        type=str,
        required=True,
    )

    return parser.parse_args()


def plot_BarChart(df: DataFrame, filename: str) -> None:
    data: dict = {}
    columnCount: int = df.shape[0]
    lastDay: int = df.iloc[columnCount - 1]["day"] + 1

    day: int
    for day in range(lastDay):
        data[day] = df[df["day"] == day]["author_email"].unique().shape[0]

    figure: Figure = plt.figure()

    plt.ylabel("Number of Contributors")
    plt.xlabel("Days")
    plt.title("Contributor Count per Day")

    plt.bar(list(data.keys()), [data[day] for day in range(lastDay)])
    figure.savefig(filename)


def loadDataFrame(filename: str) -> DataFrame:
    return pandas.read_json(filename)


def main() -> None:
    args: Namespace = get_argparse()

    if args.input[-5::] != ".json":
        print("Invalid input file type. Input file must be JSON")
        quit(1)

    json: Any = loadDataFrame(args.input)
    plot_BarChart(json, args.output)


if __name__ == "__main__":
    main()
