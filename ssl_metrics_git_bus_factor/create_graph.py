from argparse import ArgumentParser, Namespace

import pandas
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.figure import Figure

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
    figure: Figure = plt.figure()
    plt.ylabel("Number of Contributors")
    plt.xlabel("Day Since Repo Initalization")
    plt.title("Bus Factor")
    plt.bar([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    figure.savefig(filename)

def loadData(filename: str) ->  DataFrame:
    return pandas.read_json(filename)


def main() -> None:
    args: Namespace = get_argparse()

    if args.input[-5::] != ".json":
        print("Invalid input file type. Input file must be JSON")
        quit(1)

    df: DataFrame = loadData(args.input)
    plot_StackedBarChart(df, args.output)

if __name__ == "__main__":
    main()
