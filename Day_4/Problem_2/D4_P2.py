import os
from typing import Literal

DIRECTORY_PATH = os.path.abspath(os.path.join(__file__, "..", ".."))
FILE_NAME: Literal["example.txt", "input.txt"] = "input.txt"

def check_X(letter_pos: tuple[int, int]):
	global word_search_array
	possible_lists = [['M', 'M', 'A', 'S', 'S'], ['M', 'S', 'A', 'M', 'S'], ['S', 'S', 'A', 'M', 'M'], ['S', 'M', 'A', 'S', 'M']]
	size0 = len(word_search_array[0])
	size1 = len(word_search_array)
	if letter_pos[0] + 1 < size0 and letter_pos[0] - 1 >= 0 and letter_pos[1] + 1 < size1 and letter_pos[1] - 1 >= 0:
		letter_list = [word_search_array[letter_pos[0] + 1][letter_pos[1] - 1], word_search_array[letter_pos[0] + 1][letter_pos[1] + 1], word_search_array[letter_pos[0]][letter_pos[1]], word_search_array[letter_pos[0] - 1][letter_pos[1] - 1], word_search_array[letter_pos[0] - 1][letter_pos[1] + 1]]
		if letter_list in possible_lists:
			return 1
	return 0

total = 0
word_search_array = []
possition_array = []
row = 0
with open(DIRECTORY_PATH + "\\" + FILE_NAME, "r") as file:
	for line in file:
		column = 0
		for letter in line:
			if letter == 'A':
				possition_array.append((row, column))
			column += 1
		word_search_array.append(list(line.strip()))
		row += 1

for letter_pos in possition_array:
    total += check_X(letter_pos)

print(f"XMAS occurrences: {total}")
