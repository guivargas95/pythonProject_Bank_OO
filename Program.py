class Program:
    def __init__(self, name, year):

        self._likes = 0
        self._name = name.title()
        self._year = year

    @property
    def name(self):
        return self._name

    @property
    def year(self):
        return self._year

    @property
    def likes(self):
        return self._likes

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    @year.setter
    def year(self, new_year):
        self._year = new_year

    def add_like(self):
        self._likes += 1

    def __str__(self):
        return f"Name: {self.name}\nYear: {self.year}\nLikes: {self.likes}"


class Movies(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f"Name: {self.name}\nYear: {self.year}\nDuration: {self.duration}\nLikes: {self.likes}"


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f"Name: {self.name}\nYear: {self.year}\nSeasons: {self.seasons}\nLikes: {self.likes}"


movie1 = Movies("matrix", 1995, "120")
series1 = Series("supernatural", 2002, "16")

movie1.add_like()
movie1.add_like()
series1.add_like()
program_list = [movie1, series1]

for program in program_list:
    print(program)
