import os
from typing import Literal

DIRECTORY_PATH = os.path.abspath(os.path.join(__file__, "..", ".."))
FILE_NAME: Literal["example.txt", "input.txt"] = "input.txt"

with open(DIRECTORY_PATH + "\\" + FILE_NAME, "r") as file:
    list_group1: list[int] = []
    list_group2: list[int] = []
    for line in file:
        value1, value2 = map(int, line.strip().split())
        list_group1.append(value1)
        list_group2.append(value2)

list_group1.sort()
list_group2.sort()
total = 0
for value1, value2 in zip(list_group1, list_group2):
	total += abs(value1 - value2)
print(f"Total distance: {total}")
