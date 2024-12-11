import os
from typing import Literal

DIRECTORY_PATH = os.path.abspath(os.path.join(__file__, "..", ".."))
FILE_NAME: Literal["example.txt", "input.txt"] = "input.txt"

total = 0
iterator = 0
coords = [0, 0]
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
array = []
with open(DIRECTORY_PATH + "\\" + FILE_NAME, "r") as file:
	for line in file:
		array.append([val for val in line.strip()])
		if '^' in line:
			coords[0]= iterator
			coords[1] = array[iterator].index('^')
		iterator += 1

actual_direction = 0
out = False
while not out:
	if array[coords[0]][coords[1]] != 'X':
		total += 1
		array[coords[0]][coords[1]] = 'X'
	new_coords = (coords[0] + directions[actual_direction][0], coords[1] + directions[actual_direction][1])
	try:
		if array[new_coords[0]][new_coords[1]] == '#':
			actual_direction = (actual_direction + 1) % 4
		else:
			coords = new_coords
	except:
		out = True

print(f"Sum of all correct updates: {total}")
