#!/usr/bin/python3
def element_at(my_list, idx):
<<<<<<< HEAD
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    else:
        return my_list.pop(idx)
=======
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
>>>>>>> 93373a7b2ff75fbae4c47b55b6eda428ca4243a4
