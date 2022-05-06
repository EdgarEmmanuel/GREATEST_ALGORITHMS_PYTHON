class Country:
    def __init__(self, countries):
        self.countries = countries

    def __iter__(self):
        return CountryIterable(self.countries)

class CountryIterable:
    def __init__(self, countries):
        self.countries_upper = [country.capitalize() for country in countries]
        self.index = 0

    def __next__(self):
        if self.index == len(self.countries_upper):
            raise StopIteration()

        country = self.countries_upper[self.index]
        self.index +=1
        return country

    def __iter__(self):
        return self

iterable = iter(Country(['japan', 'ghana', 'usa', 'france']))

while True:
    try:
        current = next(iterable)
        print(current)
    except StopIteration:
        break