#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
<<<<<<< HEAD
    if my_list:
        for elm in my_list[::-1]:
            print("{:d}".format(elm))
=======
    if my_list is None:
        return None
    for i in reversed(my_list):
        print("{:d}".format(i))
>>>>>>> 93373a7b2ff75fbae4c47b55b6eda428ca4243a4
