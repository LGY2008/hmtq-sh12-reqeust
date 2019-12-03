import yaml


def read_yaml(filename):
    with open("./data/" + filename, "r", encoding="utf-8") as f:
        arr = []
        for data in yaml.load(f).values():
            arr.append(tuple(data.values()))
        return arr
