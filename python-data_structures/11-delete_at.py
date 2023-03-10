#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
<<<<<<< HEAD
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
=======
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
>>>>>>> 93373a7b2ff75fbae4c47b55b6eda428ca4243a4
    return my_list
