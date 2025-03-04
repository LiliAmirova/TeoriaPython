# Tuple (КОРТЕЖ)-это список, который нельзя изменить после его создания

# Справочно:
values = [10, 'число', 4, 9]  # список
list_dict = {0: 10, 1: "число", 2: 4, 3: 9}  # словарь-частный случай списка
dict = {"car": "машина", "dog": "собака", "cat": "кошка"}  # словарь
# ##################################################################

a=(1,2)          # кортеж/tuple
b=(2,)           # кортеж из 1-го элемента
c=(3)            # это НЕ кортеж-это целое число
d=1, 2, 3, 4     # еще один способ создания кортежа
e=()             # создание пустого картежа
g=tuple()        # другой способ создания кортежа
f=tuple([1,2,3]) # создание кортежа из списка
h=tuple('Hello student') # создание кортежа из строки

print(a,type(a)) # вывод кортежа и тип элемента
print(b,type(b)) # вывод кортежа из одного элемента
print(c,type(c)) # вывод целого числа
print(d, type(d)) # создание кортежа другим способом
print(e, type(e)) # вывод пустого кортежа
print(g, type(g)) # вывод пустого кортежа, созданного другим способом
print(f, type(f)) # вывод кортежа из списка
print(h, type(h)) # вывод кортежа из строки

a10 = [1, 4, 'hello', [1, 2, 3, 4], True]         # список
b10= tuple([1, 4, 'hello', [1, 2, 3, 4], True])  # кортеж из списка

print("Определение типа элемента:", a10, type(a10))
print(b10, type(b10))

print("Измерение размера списка:", a10.__sizeof__())  # функция для измерения размера
print("Измерение размера кортежа:", b10.__sizeof__())  # функция для измерения размера

# действия с кортежами

c = (1, 4, 'hello', [1, 2, 3, 4], True)  # кортеж
d = tuple([1, 2, 3, 4])  # кортеж из списка

print(c.__sizeof__())  # измерение размера обычного кортежа

print("Сложение кортежей c+d:", c + d)
print("Умножение кортежа на число:", d * 3)

# проверка наличия элемента в кортеже  print(2 in d)

print("Проверка наличия элемента в кортеже:", 2 in b)
print("Проверка отсутствия элемента в кортеже:", 2 not in b)

