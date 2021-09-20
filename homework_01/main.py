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

def is_prime(num):
    if num==2 or num==3: return True
    if num%2==0 or num<2: return False
    for i in range(3, int(num**0.5)+1, 2):
        if num%i==0:
            return False
    return True

def filter_odd(num):
        if num % 2 != 0:
            return True
        else:
            return False

def filter_numbers(list_of_nums, key=None):
    if key == ODD:
        return list(filter(filter_odd, list_of_nums))
    elif key == EVEN:
        return list(filter(lambda v: not filter_odd(v), list_of_nums))
    elif key == PRIME:
        return list(filter(is_prime, list_of_nums))
    else:
        return "Second argument is required and should be one of the following:\nODD\nEVEN\nPRIME"

print(filter_numbers([1,2,3,4,5,6,7,8,9,10,11,12,13],EVEN))
#print(is_prime(13))