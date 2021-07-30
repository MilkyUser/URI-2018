# URI - 2018
## Olímpiadas de Natal

This module implements the resolution the URI - 2018 problem (Olimpíadas de Natal).
It can also be used to implement a counting and sorting system for medals in competitions and olympics using the `CountryMedals` class.

## CountryMedals

A class to hold the information of a particular country. It has the following declared variables:

- `self.name`: which holds the name of the country as a string
- `self.gold_medals`, `self.silver_medals` and `bronze_medals`: each holds a list containing the modalities (as strings) which this country has won

### Class methods

- `add_medal(self, modality: str, medal: [str, int]) -> None` :
    - This method adds a single medal to a `CountryMedals` object.
    - It receives a string that represents the modality and either a int or str to represent the type of the medal
- `done_better_than(self, opponent: CountryMedals) -> bool`:
  - This method compares two `CountryMedals` objects (itself, and other as an argument).
  - It compares first which country has more gold medals, then silver, then bronze, sequentially and using each less important medal as an untying way
  - If the two countries have the same amount of each medal it then compares the names (using alphabetic order)

## Module methods

- `sort_countries(countries: List[CountryMedals])`:
  - This function uses a bubble sort algorithm - not really useful for large sets of data
- `_main()`: this function implements the resolution the URI problem itself. Runs in the terminal whenever the module is called from the console