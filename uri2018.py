# This module implements the resolution the URI - 2018 problem (Olimpíadas de Natal)
# It can also be used to implement a counting and sorting system for medals in competitions
# and olympics.

from __future__ import annotations
from typing import List
import sys


class CountryMedals:

    def __init__(self, name: str, medals: List[list[str]] = None):

        if medals is None:
            medals = [[], [], []]
        self.name = name
        self.gold_medals = medals[0]
        self.silver_medals = medals[1]
        self.bronze_medals = medals[2]

    def __repr__(self):
        return {'name': self.name, 'gold medals': self.gold_medals,
                'silver medals': self.silver_medals, 'bronze medals': self.bronze_medals}.__str__()

    def add_medal(self, modality: str, medal: [str, int]) -> None:

        if isinstance(medal, str):
            if medal.lower() == 'gold':
                self.gold_medals.append(modality)
            elif medal.lower() == 'silver':
                self.silver_medals.append(modality)
            elif medal.lower() == 'bronze':
                self.bronze_medals.append(modality)

        elif isinstance(medal, int):
            if medal == 0:
                self.gold_medals.append(modality)
            elif medal == 1:
                self.silver_medals.append(modality)
            elif medal == 2:
                self.bronze_medals.append(modality)

        else:
            raise TypeError(medal)

    def done_better_than(self, opponent: CountryMedals) -> bool:

        # Compare gold
        if len(self.gold_medals) > len(opponent.gold_medals):
            return True

        if len(self.gold_medals) < len(opponent.gold_medals):
            return False

        # Compare silver
        if len(self.silver_medals) > len(opponent.silver_medals):
            return True

        if len(self.silver_medals) < len(opponent.silver_medals):
            return False

        # Compare bronze
        if len(self.bronze_medals) > len(opponent.bronze_medals):
            return True

        if len(self.bronze_medals) < len(opponent.bronze_medals):
            return False

        # Compare names
        return self.name < opponent.name


def sort_countries(countries: List[CountryMedals]):
    sorted_countries = [countries[0]]

    # this function uses a bubble sort algorithm - not really useful for large sets of data
    for country in countries[1:]:
        added = False
        for i, sorted_country in enumerate(sorted_countries):
            if country.done_better_than(sorted_country):
                sorted_countries.insert(i, country)
                added = True
                break
        if not added:
            sorted_countries.append(country)
    return sorted_countries


def _main() -> None:
    raw_input = sys.stdin.readlines()
    countries = dict()

    # builds the countries dictionary
    for i in range(1, len(raw_input), 4):
        for j in range(3):
            key = ''.join(filter(lambda a: a != '\n', raw_input[i + j]))
            if key not in countries:
                countries[key] = [[], [], []]
            countries[key][j].append(''.join(filter(lambda a: a != '\n', raw_input[i-1])))

    # converts the dictionary to a list of CountryMedals objects
    countries = [CountryMedals(key, value) for key, value in countries.items()]

    print('Quadro de Medalhas')
    [print(country.name, len(country.gold_medals), len(country.silver_medals), len(country.bronze_medals))
     for country in sort_countries(countries)]


if __name__ == '__main__':
    _main()
