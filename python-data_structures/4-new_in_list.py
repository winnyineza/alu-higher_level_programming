#!/usr/bin/python3
def new_in_list(my_list, idx, element):
<<<<<<< HEAD
    listlength = len(my_list) - 1
    if (idx < 0 or idx > listlength):
        return (my_list)
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return (new_list)
=======
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
>>>>>>> 93373a7b2ff75fbae4c47b55b6eda428ca4243a4
