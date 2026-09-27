import pathlib


def enabled(name):
    text = pathlib.Path(__file__).parents[2].joinpath("config", "flags.yaml").read_text()
    return f"{name}: true" in text
