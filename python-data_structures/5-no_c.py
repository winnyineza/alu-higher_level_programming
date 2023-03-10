#!/usr/bin/python3
def no_c(my_string):
<<<<<<< HEAD
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    return new_string
=======
    # Initialize an empty string to store the result
    result = ""
    # Iterate over each character in the string
    for c in my_string:
        # Check if the character is not 'c' or 'C'
        if c != 'c' and c != 'C':
            # If it's not, add it to the result
            result += c
    # Return the result string
    return result
>>>>>>> 93373a7b2ff75fbae4c47b55b6eda428ca4243a4
