import os
from typing import Literal

DIRECTORY_PATH = os.path.abspath(os.path.join(__file__, "..", ".."))
FILE_NAME: Literal["example.txt", "input.txt"] = "input.txt"

def check_line(array: list[int]) -> bool:
	global rules
	sub_array = []
	for value in array:
		for previous in sub_array:
			try:
				if previous in rules[value]:
					return False
			except:
				continue
		sub_array.append(value)
	return True

rules = {}
total = 0
with open(DIRECTORY_PATH + "\\" + FILE_NAME, "r") as file:
	line = file.readline()
	while line.strip() != "":
		val1, val2 = map(int, line.strip().split("|"))
		try:
			rules[val1].append(val2)
		except:
			rules[val1] = [val2]
		line = file.readline()
	for line in file:
		array = list(map(int, line.strip().split(',')))
		correct_line = check_line(array)
		if correct_line:
			total += array[len(array) // 2]

print(f"Sum of all correct updates: {total}")
