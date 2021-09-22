from json import load


def loadJSON(filename: str) -> list:
    with open(file=filename, mode="r") as file:
        return load(file)


def buildBusFactor(commits: list) -> list:
    data: dict = {}

    commit: dict
    for commit in commits:
        day: int = commit["day_since_0"]
        authorName: str = commit["author_name"]
        authorEmail: str = commit["author_email"]
        authorLOC: int = abs(commit["delta_loc"])

        try:
            if type(data[day]) is list:
                HAS_RECORD: bool = False

                record: dict
                for record in data[day]:
                    if record["author_email"] == authorEmail:
                        record["loc"] += authorLOC
                        record["commits"] += 1
                        HAS_RECORD = True
                        break

                if HAS_RECORD == True:
                    continue
                else:
                    data[day].append(
                        {
                            "author_email": authorEmail,
                            "author_name": authorName,
                            "loc": authorLOC,
                            "commits": 1,
                        }
                    )

        except KeyError:
            data[day] = []
    print(data)


def main() -> None:
    data = loadJSON("commits.json")
    buildBusFactor(data)


if __name__ == "__main__":
    main()
