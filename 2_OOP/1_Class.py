# ООП-Объектно-ориентированное программирование
# Идея ООП: к осн программе подключаются НЕ функции, а ОБЪЕКТЫ, внутри которых лежат собственные переменные и функции
# Класс - это шаблон для создания объектов (экземпляров класса), которые описывает св-ва(атрибуты) и действия (методы),
# могут обладать все объекты этого класса
# Название классов в ЕДИНСТВЕННОМ числе + с БОЛЬШОЙ буквы
# Название файла-как название Класса (правило)
# https://habr.com/ru/companies/yandex_praktikum/articles/749180/

class ClassName:  # Ключевое слово class и имя класса.
    # Тело класса
    pass


class HockeyPlayer:
    # Атрибут класса:
    default_position = 'Forward'

    # Конструктор класса (специальный метод):
    def __init__(self, name, surname, age, team):
        # Атрибуты экземпляра класса:
        self.name = name
        self.surname = surname
        self.age = age
        self.team = team

        # Метод экземпляра класса:

    def get_full_name(self):
        return f'{self.name} {self.surname}'


# # # # # # #
class Rich_uncle:
    def __init__(self):
        pass


# # # # # # # БЕЗ передачи ПЕРЕМЕННЫх атрибутам класса
class Rich_uncle:
    def __init__(self):
        self.balance = 9000
        self.country = 'Italy'


uncle_john = Rich_uncle()
print(uncle_john.balance)
print(uncle_john.country)

uncle_john.balance = 10  # переопределение значение атрибута
uncle_sam = Rich_uncle()

print(uncle_john.balance)
print(uncle_sam.balance)


# # # # # # # Передача ПЕРЕМЕННЫХ для атрибутов класса
class Rich_uncle:
    def __init__(self, balance, country):
        self.balance = balance
        self.country = country


uncle_john = Rich_uncle(4000, 'Italy')
uncle_sam = Rich_uncle(1000, 'USA')

print(uncle_john.balance, uncle_john.country)
print(uncle_sam.balance)


# # # # # # # Создание функции/методов для класса
class Rich_uncle:
    def __init__(self, balance, country, name):
        self.balance = balance
        self.country = country
        self.name = name

    def get_private_plane(self):
        print(f'Сэр {self.name}, ваш самолет ждет вас!')


uncle_john = Rich_uncle(4000, 'Italy', 'Джон')
uncle_sam = Rich_uncle(1000, 'USA', 'Сэм')

uncle_john.get_private_plane()
uncle_sam.get_private_plane()


# # # # # # # Передача значение ФУНКЦИИ по УМОЛЧАНИЮ (прописывается в конце)
class Rich_uncle:
    def __init__(self, country, name, balance=90000):
        self.balance = balance
        self.country = country
        self.name = name

    def get_private_plane(self):
        print(f'Сэр {self.name}, ваш самолет ждет вас!')

    def get_balance(self):
        print(f'У меня на балансе: {self.balance} долларов')


uncle_john = Rich_uncle('Italy', 'Джон')
uncle_sam = Rich_uncle('USA', 'Сэм')

uncle_john.get_balance()
uncle_sam.get_balance()
# # # # # Изменить значение атрибута заданного по умолчанию в функции
uncle_roy = Rich_uncle('China', 'Ли', 500)
uncle_roy.get_balance()
