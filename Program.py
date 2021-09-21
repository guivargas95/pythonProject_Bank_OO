class Program:
    def __init__(self, name, year, additional_information="undefined"):
        self.__name = name.title()
        self.__year = year
        self.__additional_information = additional_information

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    @property
    def additional_information(self):
        return self.__additional_information

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    @additional_information.setter
    def additional_information(self, new_information):
        self.__additional_information = new_information


class Movie(Program):
    def __init__(self, name, year, additional_information):
        super().__init__(name, year)
        self.additional_information = additional_information


program1 = Program("matrix", 1995, "150")
print(program1.name)
program1.name = "matrix reloaded"
print(program1.name)
