## Исключения (Exceptions)
# Любой экстренный выход из выполнения программы-это НЕ хорошо
# т.е. все исключения, который потенциально могут быть должны быть обработаны должным образом
# Exception-это родитель  для всех exceptions

# a='10ad'
# print(int(a))   # выйдет ошибка типа: ValueError: invalid literal for int() with base 10: '10ad'

# # # #  Обработка одного ОПРЕДЕЛЕННОГО исключения
try:
    a='10ad'
    print(int(a))
except ValueError as e:
    print('Получена ошибка ValueError:', e.args)

# # # # #Обработка нескольких ОПРЕДЕЛЕННЫХ исключений
try:
    b='10ad'
    c=10/0  #  получим ошибку: ZeroDivisionError: division by zero
    print(int(b))

except (ValueError,ZeroDivisionError) as e: # в скобках написаны 2 вида исключений, которые обрабатываются
    print('Получена ошибка:', e.args)

# # # # # Обработка исключения, когда НЕ знаете какой Exception можете поймать, то можно написать в общем виде:
try:
    d='10ad'
    h=10/0  #  получим ошибку: ZeroDivisionError: division by zero
    print(int(d))

except Exception as e: # в скобках написаны 2 вида исключений, которые обрабатываются
    print('Получена ошибка:', e.args)

# # # # # # Обработка каждого ИСКЛЮЧЕНИЯ по отдельности с выводом своего текста
try:
    a1='10ad'
    c1=10/0  #  получим ошибку: ZeroDivisionError: division by zero
    print(int(a1))
except (ValueError,) as e: # в скобках написаны 2 вида исключений, которые обрабатываются
    print('Получена ошибка ValueError:', e.args)
except (ZeroDivisionError) as e:  # в скобках написаны 2 вида исключений, которые обрабатываются
    print('Получена ошибка ZeroDivisionError:', e.args)

# # # # # # БЛОК Finally-который выполняется ВСЕГДА ( в любом случае)
try:
    a2='10ad'
    #c2=10/0  #  получим ошибку: ZeroDivisionError: division by zero
    print(int(a2))
except (ValueError,) as e: # в скобках написаны 2 вида исключений, которые обрабатываются
    print('Получена ошибка ValueError:', e.args)
except (ZeroDivisionError) as e:  # в скобках написаны 2 вида исключений, которые обрабатываются
    print('Получена ошибка ZeroDivisionError:', e.args)
finally:
    print('Я блок finally, который выполняется всегда')

# # # # # # Else-выполниться в случае если НЕ будет выполнен Exception (пишется между Exception и finally)
try:
    a2='10ad'
    #c2=10/0  #  получим ошибку: ZeroDivisionError: division by zero
    #print(int(a2))
except (ValueError,) as e: # в скобках написаны 2 вида исключений, которые обрабатываются
    print('Получена ошибка ValueError:', e.args)
except (ZeroDivisionError) as e:  # в скобках написаны 2 вида исключений, которые обрабатываются
    print('Получена ошибка ZeroDivisionError:', e.args)
else:              # выполняется, когда нет ошибок
    print('Исключения не появились, код работает отлично')
finally:
    print('Я блок finally, который выполняется всегда')