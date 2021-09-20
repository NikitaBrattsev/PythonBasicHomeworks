"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    result = []
    for num in nums:
        result.append(num*num)
    return result
    

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(list_of_nums, key=None):
    def filter_odd(num):
        if num % 2 != 0:
            return True
        else:
            return False
    if key == ODD:
        return list(filter(filter_odd,list_of_nums))
    elif key == EVEN:
        return list(filter(lambda v: not filter_odd(v),list_of_nums))
    else:
        return "Second argument is required and should be one of the following:\nODD\nEVEN"

#print(filter_numbers([1,2,3,4,5,6],ODD))