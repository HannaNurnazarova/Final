#Написать программу, которая из имеющегося массива строк формирует
# новый массив из строк, длина которых меньше, либо равна 3 символам. 
# Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма.
# При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.

def filter_short_strings(strings):
    short_strings = ["dog", "cat", "open", "string"]
    for string in strings:
        if len(string) <= 3:
            short_strings.append(string)
    return short_strings
input_strings = input("Введите строки, разделенные пробелами: ").split()
result_strings = filter_short_strings(input_strings)
print("Строки длиной <= 3 символов:", result_strings)

