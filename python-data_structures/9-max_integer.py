#!/usr/bin/python3
def max_integer(my_list=[]):
<<<<<<< HEAD
    length = len(my_list)

    if length == 0:
        return (None)

    max_int = my_list[0]

    for i in range(1, length):
        if my_list[i] > max_int:
            max_int = my_list[i]

    return (max_int)
=======
    if not my_list:
        return None
    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value
>>>>>>> 93373a7b2ff75fbae4c47b55b6eda428ca4243a4
