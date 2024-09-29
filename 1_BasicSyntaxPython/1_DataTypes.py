#Типы данных: integer, float, boolean, string, list, dictionary

    number = 100          #integer
    number_float = 10.5   #float-с плавающей запятой

    text = 'ТЕКСТ'
    text_another = "ТЕКСТ"
    text1 = 'Цитата: "Программировать легко"'      # двойные кавычки внутри одинарных кавычек
    text2 = "Цитата: \"Программировать легко\""    #двойные кавычки ВНУТРИ двойных с ЭКРАНИРОВАНИЕМ
    text3 = 'Цитата: \'Программировать легко\''    #одинарные кавычки внутри одинарных с ЭКРАНИРОВАНИЕМ
    # print(text3)

    boolean_value = True  # boolean-логический тип данных
    another_boolean_value = False

    # print(number+number_float) -все ОК
    # print(number+text) -НЕ ок нельзя
    # print(number+boolean_value)- Все ок , boolean_value = True =1,  another_boolean_value = False=0

    values = 10, 36, 4, 9     # list-списки
    # print("вывод всего списка:",values)-вывод всего списка
    print(values[0])

    another_number="100" # string
    text="цитата"        # string
    number=100           # integer

    a, b, c = 20, 10, 56   # ФИШКА: объявление нескольких переменных

    values=[10,'число',4,9]                                #список
    list_dict={0:10, 1:"число", 2:4, 3:9}                  #словарь-частный случай списка
    dict={"car":"машина", "dog":"собака", "cat": "кошка"}  #словарь

    print(values[1])
    print(list_dict[0])
    print(dict["dog"])

    print(another_number+text)             # сложение строковой переменных
    print(number, another_number)          # Вывод переменных РАЗНОГО типа

    print(number, another_number, text,)    # по умолчанию ПРОБЕЛ
    print(number, another_number, text, sep='разделитель')   # ФИШКА: разделитель при выводе элементов

