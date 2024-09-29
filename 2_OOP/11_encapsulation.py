# Инкапсуляция-это сокрытие реализации

class rich_uncle:
    def __init__(self, name, balance=9000):
        self.__balance=balance    # инкапсуляция, теперь напрямую мы не сможем обратиться к атрибуту
        self.country='Italy'
        self.name=name

# uncle_john=rich_uncle('Джон',1000) # AttributeError: 'rich_uncle' object has no attribute 'balance'
# uncle_john.__balance=1000  # Получаем ошибку: AttributeError: 'rich_uncle' object has no attribute 'balance'. Did you mean: '__balance'
uncle_john=rich_uncle('Джон')
uncle_john.balance=1000

print(uncle_john.balance) # Почему нет ошибки???????


