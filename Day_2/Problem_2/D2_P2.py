import os
from typing import Literal

DIRECTORY_PATH = os.path.abspath(os.path.join(__file__, "..", ".."))
FILE_NAME: Literal["example.txt", "input.txt"] = "input.txt"

def is_safe(array: list[int]):
	iterator = 0
	increasing = None
	while iterator < len(array) - 1:
		value1 = array[iterator]
		value2 = array[iterator + 1]
		if increasing is None:
			if value1 == value2:
				return False
			else:
				increasing = value1 < value2
		else:
			if value1 == value2 or increasing != (value1 < value2) or abs(value1 - value2) > 3:
				return False
			iterator += 1
	return True

def safe_by_removing(array: list[int]):
	iterator = 0
	while iterator < len(array):
		aux_value = array[iterator]
		array.pop(iterator)
		if is_safe(array):
			return True
		array.insert(iterator, aux_value)
		iterator += 1
	return False

total = 0
with open(DIRECTORY_PATH + "\\" + FILE_NAME, "r") as file:
	for line in file:
		values = list(map(int, line.strip().split()))
		if is_safe(values) or safe_by_removing(values):
			total += 1

print(f"Safe reports: {total}")
