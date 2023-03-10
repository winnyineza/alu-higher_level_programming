#!/usr/bin/python3
def multiple_returns(sentence):
<<<<<<< HEAD
    len_sen = len(sentence)

    if (len_sen == 0):
        new_tuple = (len_sen, None)
    else:
        new_tuple = (len_sen, sentence[0])

    return (new_tuple)
=======
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
>>>>>>> 93373a7b2ff75fbae4c47b55b6eda428ca4243a4
