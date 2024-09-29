# Абстракция
# Абстрактный класс- это класс, который объясняет как и что должно быть реализовано, но при этом в абстрактном классе ничего НЕ реализовано

from abc import ABC

class car(ABC):       # Абстрактный класс
    def __init__(self):
        self.hp=250

    def drive(self):   # методы НЕ определены
        pass
    def stop(self):    # методы НЕ определены
        pass
    def lights(self):  # методы НЕ определены
        pass

class niva(car):       #  Определяем функции
    def drive(self):   # методы НЕ определены
        print('Едим')
    def stop(self):    # методы НЕ определены
        print('Тормозим')
    def lights(self):  # методы НЕ определены
        print('Светим')

niva_legend=niva()

niva_legend.drive()
niva_legend.lights()
niva_legend.stop()

