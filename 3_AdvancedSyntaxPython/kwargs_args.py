# Продвинутые функции: args / kwargs

# Функция с указанием типа ПЕРЕМЕННЫХ
def add(a:int, b:int):
    print(a+b)
add(2,3)     # Вызов функции с указанием параметров переменных

# # # # # # args: Модификация функции: сложение всего что придет в аргумент

def add_all(*args):
    all_summary=0
    for num in args:
        all_summary+=num
    return all_summary

values=[1,2,3,4,5,6]
more_values=[10,20,30,40,50,60]
print(add_all(*values))               # сложение одного списка (* -раскрывает список)
print(add_all(*values,*more_values))  # сложение двух списков


# # # # # # kwargs:Получение словаря в виде: {....}
def authtorize(**kwargs):
    print('Вывод в виде словаря :')
    print(kwargs)
authtorize(name='Liliia', age='45', job='AQA')
print()

# # # # # #  вывод отдельно ключ и значение
def aut(**kwargs):
    print('вывод отдельно ключ и значение:')
    for key, value in kwargs.items():
        print(key)
        print(value)
aut(name='Amirova', age='45', job='AQA')
print()

# # # # # # Другой способ передачи kwargs
def autt(**kwargs):
    print('Другой способ передачи kwargs')
    for key, value in kwargs.items():
        print(key)
        print(value)

data={'name': 'Liliia', 'age': '45', 'job': 'AQA'}
autt(**data)