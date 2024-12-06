import os
from typing import Literal

DIRECTORY_PATH = os.path.abspath(os.path.join(__file__, "..", ".."))
FILE_NAME: Literal["example.txt", "input.txt"] = "input.txt"

with open(DIRECTORY_PATH + "\\" + FILE_NAME, "r") as file:
    list_group1: list[int] = []
    coincidences: dict = {}
    for line in file:
        value1, value2 = map(int, line.strip().split())
        list_group1.append(value1)
        try:
            coincidences[value2] += 1
        except:
            coincidences[value2] = 1

total = 0
for value in list_group1:
    try:
        total += value * coincidences[value]
    except:
        continue
print(f"Similarity score: {total}")
