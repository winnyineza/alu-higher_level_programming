#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""

import json
import sys
from os import path
from typing import List

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(filename: str, args: List[str]):
    """Adds all arguments to a Python list and saves them to a file"""
    new_list = []
    if path.exists(filename):
        new_list = load_from_json_file(filename)
    new_list += args
    save_to_json_file(new_list, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    add_item("add_item.json", args)
