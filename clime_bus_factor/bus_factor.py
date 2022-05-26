from argparse import Namespace

import pandas
from pandas import Categorical, DataFrame, Interval, Series

from clime_bus_factor.args import developerCountArgs

def buildBusFactor(df: DataFrame, *, bin: int, alpha: float = 0.0) -> DataFrame:
    day_key = "author_days_since_0"
    lastday = df[day_key].max() + bin
    bins = list(range(0, lastday, bin))

    df["commitBin"] = pandas.cut(df[day_key], bins=bins, include_lowest=True)
    bins = df["commitBin"].unique().tolist()

    data = []
    for bin in bins:

        item = {"days_since_0": int(bin.left) if bin.left > 0 else 0}

        if alpha:
            temp = df[df["commitBin"] == bin]
            abs_list = lambda l: [abs(item) for item in l]
            significance = alpha * sum(abs_list(temp["dkloc"].tolist()))

            bf = 0
            authors = set(temp["author_email"].tolist())
            for author in authors:
                author_dloc = sum(
                    abs_list(temp[temp["author_email"] == author]["dkloc"].tolist())
                )
                if author_dloc > significance:
                    bf += 1

            temp = temp[temp["dkloc"] > significance]

            item["busFactor"] = bf
        else:
            item["devs"] = len(df[df["commitBin"] == bin]["author_email"].unique())

        data.append(item)

    return DataFrame(data)

def main() -> None:
    args: Namespace = developerCountArgs()

    if args.bin < 1:
        print(f"Bin arguement must be an integer greater than 0: {args.bin}")
        quit(1)
    if args.alpha > 1:
        print("Invalid alpha value. Must be alpha =< 1 and alpha >= 0")
        quit(2)
    if args.alpha < 0:
        print("Invalid alpha value. Must be alpha =< 1 and alpha >= 0")
        quit(3)

    df: DataFrame = pandas.read_json(args.input).T
    bf: DataFrame = buildBusFactor(df, bin=args.bin, alpha=args.alpha)
    cd: DataFrame = buildBusFactor(df, bin=args.bin, alpha=0)

    pandas.concat([bf, cd]).to_json(args.output, indent=4)


if __name__ == "__main__":
    main()
