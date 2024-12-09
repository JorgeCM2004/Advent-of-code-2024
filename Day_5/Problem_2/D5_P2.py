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

def correct_line(array: list[int]) -> list[int]:
	global rules
	while not check_line(array):
		sub_array = []
		index_array = 0
		changed = False
		while index_array < len(array) and not changed:
			value = array[index_array]
			index_sub_array = 0
			while index_sub_array < len(sub_array) and not changed:
				previous = sub_array[index_sub_array]
				try:
					if previous in rules[value]:
						index_previous = array.index(previous)
						array.remove(value)
						array.insert(index_previous, value)
						changed = True
				except:
					index_sub_array += 1
					continue
				index_sub_array += 1
			index_array += 1
			sub_array.append(value)
	return array

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
		is_correct = check_line(array)
		if not is_correct:
			array = correct_line(array)
			total += array[len(array) // 2]

print(f"Sum of all correct updates: {total}")
