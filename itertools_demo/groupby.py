"""Groupby demos."""
import csv
from itertools import groupby

from pydantic.dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Population:
    city: str
    country: str
    count: int | str
    year: int | str

    def __post_init__(self):
        self.city = self.city.strip()
        self.country = self.country.strip()
        self.count = int("".join(i for i in self.count if i.isdigit()))
        self.year = int(self.year.split(" ")[2])


    @property
    def info(self) -> str:
        return f"{self.city} - population: {self.count}"

# ------------------------------------------------------------------------
def sort_and_group(iterable, *, key=None):
    """Group sorted `iterable` on `key`."""
    return groupby(sorted(iterable, key=key), key=key)

# ------------------------------------------------------------------------
def load_population() -> List[Population]:
    with open(Path(".") / "population.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter="\t", quotechar="|")
        return [Population(*population[1:5]) for population in list(reader)]


# ------------------------------------------------------------------------
def groupby_country():
    population = load_population()
    for key, group in sort_and_group(population, key=lambda population_: population_.country):
        print(f"{key}")
        for population_ in sorted(group, key=lambda population_: population_.city):
            print(f"  {population_.info}")


# ------------------------------------------------------------------------
def groupby_country_and_year():
    population = load_population()
    for key, group in sort_and_group(population, key=lambda population_: (population_.country, population_.year)):
        print(f"{key}")
        for population_ in sorted(group, key=lambda population_: population_.count, reverse=True):
            print(f"  {population_.info}")


# ------------------------------------------------------------------------
if __name__ == "__main__":
    # groupby_country()
    groupby_country_and_year()
