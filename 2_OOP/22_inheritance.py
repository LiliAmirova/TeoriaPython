# Наследование- т.е мы модем использовать все то, что доступно для класса родителя
#  у детей можем переопределить какую-нибудь функцию родителя

class rich_uncle:      # класс РОДИТЕЛЯ
    def __init__(self, name, balance=9000):
        self.__balance=balance
        self.country="Italy"
        self.name=name

    def get_balance(self):
        print(f'{self.name} имеет на балансе: {self.__balance}  долларов')

    def set_balance(self,balance):
        self.__balance=balance

    def get_private_plane(self):
        print(f'Сэр {self.name} ваш самолет ждет вас!')


class plemyannik(rich_uncle):     # класс ребенка
    def get_private_plane(self):    # переопределили функцию родителя
        print(f'Сэр, {self.name}, вам НЕ доступен самолет')

andrey=plemyannik('Андрей')
andrey.set_balance(1000)     # вызов родительской функции
andrey.get_balance()         # вызов родительской функции

andrey.get_private_plane()     # вызов переопределенной родительской функции


