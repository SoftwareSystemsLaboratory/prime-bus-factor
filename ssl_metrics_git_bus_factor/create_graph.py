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

def plot_StackedBarChart(df: DataFrame, filename: str)  ->  None:
    pass


def loadDataFrame(filename: str) -> DataFrame:
    return pandas.read_json(filename)


def main() -> None:
    args: Namespace = get_argparse()

    if args.input[-5::] != ".json":
        print("Invalid input file type. Input file must be JSON")
        quit(1)

    json: Any = loadDataFrame(args.input)


if __name__ == "__main__":
    main()
