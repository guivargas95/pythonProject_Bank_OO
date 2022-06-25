class Client:

    def __init__(self, client_id, first_name, last_name, birth):
        self.__first_name = first_name.title()
        self.__last_name = last_name.title()
        self.__birth = birth
        if self.id_validate(client_id):
            self.__client_id = client_id
        else:
            raise ValueError("Invalid ID")

    @property
    def id(self):
        return self.__client_id

    @property
    def name(self):
        return self.__first_name, self.__last_name

    @property
    def birth(self):
        return self.__birth

    @staticmethod
    def id_validate(client_id):
        first_validation = second_validation = 0
        cpf = []

        while len(client_id) != 11 or client_id in '11111111111' or client_id in '22222222222' or client_id in '33333333333' or client_id in '44444444444' or client_id in '55555555555' or client_id in '66666666666' or client_id in '77777777777' or client_id in '88888888888' or client_id in '99999999999':
            return False

        for each in client_id:
            cpf.append(int(each))

        for each, count in enumerate(range(10, 1, -1)):
            first_validation += count * cpf[each]
        first_validation = (first_validation * 10) % 11
        if first_validation == 10:
            first_validation = 0

        for each, count in enumerate(range(11, 1, -1)):
            second_validation += count * cpf[each]
        second_validation = (second_validation * 10) % 11
        if second_validation == 10:
            second_validation = 0

        if first_validation == cpf[9] and second_validation == cpf[10]:

            return True
        else:
            return False


client1 = Client("101010101010", "guilherme", "Vargas", "14071995")
print(client1.id)
print(client1.name)
