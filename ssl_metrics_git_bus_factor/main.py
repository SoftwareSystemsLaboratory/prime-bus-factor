from json import dump, load
from typing import Any

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


def fillMissingDays(data: dict) -> dict:
    days: list = list(data.keys())

    index: int
    for index in range(len(days)):
        try:
            difference: int = days[index + 1] - days[index]
            if difference == 1:
                pass
            else:
                differenceIndex: int
                for differenceIndex in range(difference):
                    if differenceIndex == 0:
                        pass
                    else:
                        data[index + differenceIndex] = []
        except IndexError:
            pass

    return data

def dumpJSON(json: Any, filename: str) -> None:
    with open(file=filename, mode="w") as file:
        dump(json, file)
        file.close()
    
def main() -> None:
    data: list = loadJSON("commits.json")
    bf: dict = buildBusFactor(data)
    bf: dict = fillMissingDays(bf)
    dumpJSON(bf, "temp.json")

if __name__ == "__main__":
    main()
