

def uppercase(func):       # декоратор-это обертка для функции, func-это параметр, обозначающий, что на вход подаем функцию
    def wrapper():
        print('Печать заглавными буквами')
        return func().upper()   # печать заглавными буквами

    return wrapper

def braces(func):         # декоратор, который заключает выводимый текст в фигурные скобки
    def wrapper():
        print('Проставляем фигурные скобки')
        return '{'+func()+'}'
    return wrapper

def square_brackets(func):
    def wrapper():
        print ('Проставляем квадратные скобки')  # логирование действий
        return  '['+func()+']'
    return wrapper

@square_brackets     # связывает декоратор и функцию
@uppercase           # порядок выполнения декораторов снизу вверх
@braces
def greet():        # Изначальная функция, которую хотим переиспользовать и модифицировать
    return 'Hello'

print(greet())
