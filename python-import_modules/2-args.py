<<<<<<< HEAD
#!/usr/bin/env python3

import sys

args = sys.argv[1:]
num_args = len(args)

if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
    print("1: {}".format(args[0]))
else:
    print("{} arguments:".format(num_args))
    for i, arg in enumerate(args):
        print("{}: {}".format(i+1, arg))

=======
#!/usr/bin/python3
from sys import argv


def principal():
    print('{} argument'.format(len(argv) - 1), end='')
    if len(argv) == 1:
        print('s.')
    elif len(argv) == 2:
        print(':')
    else:
        print('s:')
    for i in range(1, len(argv)):
        print('{}: {}'.format(i, argv[i]))


if __name__ == "__main__":
    principal()
>>>>>>> 04cfffdb128e0b746abb569fab1f8ff04369c4ad
