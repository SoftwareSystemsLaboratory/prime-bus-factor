from pandas import DataFrame
from clime_bus_factor.args import busFactorArgs
from argparse import Namespace
import pandas

def get_devs(df: DataFrame, *, bin: int, alpha=0.0) -> DataFrame:
    day_key = "day_since_0"
    lastday = df[day_key].max() + bin
    bins = list(range(0,lastday,bin))

    df["commitBin"] = pandas.cut(df[day_key], bins=bins, include_lowest=True)
    bins = df["commitBin"].unique().tolist()

    data = []
    for bin in bins:

        item = {"days_since_0" : int(bin.left) if bin.left > 0 else 0}

        if alpha:
            temp = df[df["commitBin"] == bin]
            abs_list = lambda l : [abs(item) for item in l]
            significance = alpha * sum(abs_list(temp["delta_loc"].tolist()))

            bf = 0
            authors = set(temp["author_email"].tolist())
            for author in authors:
                author_dloc = sum(abs_list(temp[temp["author_email"] == author]["delta_loc"].tolist()))
                if author_dloc > significance:
                    bf += 1

            temp = temp[temp["delta_loc"] > significance]

            item["bus_factor"] = bf
        else:
            item["devs"] = len( df[df["commitBin"] == bin]["author_email"].unique() )

        data.append(item)

    return DataFrame(data)


def main() -> None:

    args: Namespace = main_args()

    if not args.alpha:
        print(f'bus_factor calculation requires alpha value')
        quit()

    df = pandas.read_json(args.input) #.T
    bf = get_devs(df, bin=args.bin, alpha=args.alpha)
    bf.to_json(args.output, indent=4)

if __name__ == '__main__':
    main()
