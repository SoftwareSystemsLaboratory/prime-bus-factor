from argparse import Namespace

import pandas
from pandas import Categorical, DataFrame, Interval, Series

from clime_bus_factor.args import mainArgs
from clime_bus_factor.version import version


def buildBusFactor(df: DataFrame, bucket: int) -> DataFrame:
    daysSince0: Series = df["author_days_since_0"].unique()

    data: list = []

    maxDays: int = daysSince0.max() + bucket
    bucketList: list = [day for day in range(maxDays) if day % bucket == 0]

    df["commitBin"] = pandas.cut(
        df["author_days_since_0"], bins=bucketList, include_lowest=True
    )

    bins: Categorical = df["commitBin"].unique()
    binList: list = bins.tolist()

    bin: Interval
    for bin in binList:
        temp: dict = {}

        day: int = int(bin.left) if bin.left > 0 else 0

        busFactor: int = len(df[df["commitBin"] == bin]["author_email"].unique())

        temp["days_since_0"] = day
        temp["busFactor"] = busFactor

        data.append(temp)

    return DataFrame(data)


def main() -> None:
    args: Namespace = mainArgs()

    if args.version:
        print(f"clime-git-bus-factor-compute version {version()}")
        quit(0)

    if args.bucket < 1:
        print(f"Bucket arguement must be an integer greater than 0: {args.bucket}")
        quit(1)

    df: DataFrame = pandas.read_json(args.input).T
    buildBusFactor(df, bucket=args.bucket).to_json(args.output, indent=4)


if __name__ == "__main__":
    main()
