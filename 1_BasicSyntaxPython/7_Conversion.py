# Приведение типов: привести один тип к другому (н/р число в строку)
# Приведение типов: явное и НЕявное (питон сам делает без нашего участия)

# НЕявное:
a = 10  # integer
b = 3.4  # float
c = a + b
print(c, type(c))

# Явное приведение
b = str(b)
a = str(a)
print(b, type(b))
print(a, type(a))

c=5.6336
c=int(c)
c=str(c)
c=float(c)
print(c, type(c))


