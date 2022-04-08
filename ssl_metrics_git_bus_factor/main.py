from argparse import ArgumentParser, Namespace

import pandas
from pandas import DataFrame, Series


def buildBusFactor(df: DataFrame) -> DataFrame:
    daysSince0: Series = df["days_since_0"].unique()

    data: list = []

    day: int
    for day in range(daysSince0.max() + 1):
        temp: dict = {}

        busFactor: int = len(df[df["days_since_0"] == day]["author_email"].unique())

        temp["days_since_0"] = day
        temp["bus_factor"] = busFactor

        data.append(temp)
    return DataFrame(data)


def main() -> None:
    args: Namespace = get_argparse()

    if args.input[-5::] != ".json":
        print("Invalid input file type. Input file must be JSON")
        quit(1)

    dfIn: DataFrame = pandas.read_json(args.input)
    dfOut: DataFrame = buildBusFactor(df=dfIn)

    dfOut.to_json(args.output)


if __name__ == "__main__":
    main()
