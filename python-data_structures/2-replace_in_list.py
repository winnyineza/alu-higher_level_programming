#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
<<<<<<< HEAD
    if idx < 0 or idx > len(my_list) - 1:
=======
    if idx < 0 or idx >= len(my_list):
>>>>>>> 93373a7b2ff75fbae4c47b55b6eda428ca4243a4
        return my_list
    else:
        my_list[idx] = element
        return my_list
