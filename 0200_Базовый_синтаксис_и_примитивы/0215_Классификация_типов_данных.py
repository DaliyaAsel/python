"""
0215_Классификация_типов_данных
"""

x = 10
y = 3.13
x = x + 1
x = 12

s = 'hello'
print(s.capitalize)
print(s.split())
print(s.upper())
s = s + 'd'

flag = True

# коллекции / составные типы данных
numbers = [1, 2, 3]
numbers.append(4)
numbers[0] = 10
print(numbers)

t = (1, 2, 3)
s = {1, 2, 3}
s = frozenset([1, 2, 3])
d = {1: 'a', 2: 'b', 3: 'c'}

"""
неизменяемые
int
float
str
tuple
bool
frozenset
"""

"""
изменяемые
list
dict
set
"""

"""
последовательности
list
tuple
str
"""

"""
неупорядоченные
set
dict
frozenset
"""

"""
Числовые
"""
#строки
#коллекции
#bool