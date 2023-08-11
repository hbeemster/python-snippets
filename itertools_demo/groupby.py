"""Groupby demos."""
import csv
from pydantic.dataclasses import dataclass
from pathlib import Path
from datetime import date, datetime
from typing import List


@dataclass
class Population:
    country: str
    city: str
    count: int | str
    year: int | str

    def __post_init__(self):
        self.count = int("".join(i for i in self.count if i.isdigit()))
        self.year = int(self.year.split(" ")[2])


# ------------------------------------------------------------------------
def load_population() -> List[Population]:
    with open(Path(".") / "population.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter="\t", quotechar="|")
        return [Population(*population[1:5]) for population in list(reader)]


# ------------------------------------------------------------------------
def groupby_country():
    population = load_population()
    print(len(population))


# ------------------------------------------------------------------------
if __name__ == "__main__":
    groupby_country()
