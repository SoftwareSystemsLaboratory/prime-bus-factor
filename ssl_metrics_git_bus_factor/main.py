from argparse import Namespace

import pandas
from pandas import DataFrame, Series

from ssl_metrics_git_bus_factor.args import mainArgs

def buildBusFactor(df: DataFrame) -> DataFrame:
    daysSince0: Series = df["author_days_since_0"].unique()

    data: list = []

    day: int
    for day in range(daysSince0.max() + 1):
        temp: dict = {}

        busFactor: int = len(df[df["author_days_since_0"] == day]["author_email"].unique())

        temp["days_since_0"] = day
        temp["productivity"] = busFactor

        data.append(temp)

    return DataFrame(data)


def main() -> None:
    args: Namespace = mainArgs()

    df: DataFrame = pandas.read_json(args.input).T
    buildBusFactor(df).to_json(args.output)


if __name__ == "__main__":
    main()
