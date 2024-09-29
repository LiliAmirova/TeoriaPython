# Инкапсуляция
# Управление СКРЫТЫМИ параметрами через сопутствующие функции: гетры(get)  и сетры (set)

class rich_uncle:
    def __init__(self, name, balance=9000):
        self.__balance=balance
        self.country="Italy"
        self.name=name


    def get_balance(self):         # гетры
        print(f' {self.name} имеет на балансе:{self.__balance} долларов')

    def set_balance(self, balance):  # сетры
        self.__balance=balance


uncle_john=rich_uncle('Джон')
uncle_john.balance=2000
uncle_john.get_balance()     # вызов сопутствующей функции гетры

uncle_sam=rich_uncle('Сэм', 35000)

uncle_sam.set_balance(45000)  # сетры
uncle_sam.get_balance()       # сетры

