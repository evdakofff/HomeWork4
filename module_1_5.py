immutable_var = 'apple', 12, 1.5, True
print(immutable_var)

#immutable_var[0] = 'Яблоко'
#print(immutable_var)
# При выполнении такого действия получим ошибку.
# Кортежи - это неизменяемый тип данных в Python, который используется для хранения упорядоченной последовательности элементов.

mutable_list = ['Bear', 'Lion', 'Unicorn']
mutable_list[2] = 'Elephant'
print(mutable_list)