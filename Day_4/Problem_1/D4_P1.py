import os
from typing import Literal

DIRECTORY_PATH = os.path.abspath(os.path.join(__file__, "..", ".."))
FILE_NAME: Literal["example.txt", "input.txt"] = "input.txt"

def check_direction(letter_pos: tuple[int, int], direction: Literal["up", "down", "left", "right", "diagonal_pos_pos", "diagonal_pos_neg", "diagonal_neg_neg", "diagonal_neg_pos"]):
	global word_to_search
	global word_search_array
	match direction:
		case "up":
			direction0 = -1
			direction1 = 0
		case "down":
			direction0 = 1
			direction1 = 0
		case "left":
			direction0 = 0
			direction1 = -1
		case "right":
			direction0 = 0
			direction1 = 1
		case "diagonal_pos_pos":
			direction0 = -1
			direction1 = 1
		case "diagonal_pos_neg":
			direction0 = 1
			direction1 = 1
		case "diagonal_neg_neg":
			direction0 = 1
			direction1 = -1
		case "diagonal_neg_pos":
			direction0 = -1
			direction1 = -1
	word_iterator = 0
	iterator0 = 0
	iterator1 = 0
	size0 = len(word_search_array[0])
	size1 = len(word_search_array)
	while word_iterator < len(word_to_search) and letter_pos[0] + iterator0 >= 0 and letter_pos[1] + iterator1 >= 0 and letter_pos[0] + iterator0 < size0 and letter_pos[1] + iterator1 < size1:
		if word_search_array[letter_pos[0] + iterator0][letter_pos[1] + iterator1] != word_to_search[word_iterator]:
			return 0
		word_iterator += 1
		iterator0 += direction0
		iterator1 += direction1
	if word_iterator >= len(word_to_search):
		return 1
	else:
		return 0

def check_all(letter_pos: tuple[int, int]):
	letter_total = 0
	directions = ["up", "down", "left", "right",
				"diagonal_pos_pos", "diagonal_pos_neg",
				"diagonal_neg_neg", "diagonal_neg_pos"]
	for direction in directions:
		letter_total += check_direction(letter_pos, direction)
	return letter_total

total = 0
word_search_array = []
word_to_search = "XMAS"
possition_array = []
row = 0
with open(DIRECTORY_PATH + "\\" + FILE_NAME, "r") as file:
	for line in file:
		column = 0
		for letter in line:
			if letter == 'X':
				possition_array.append((row, column))
			column += 1
		word_search_array.append(list(line.strip()))
		row += 1

for letter_pos in possition_array:
    total += check_all(letter_pos)

print(f"XMAS occurrences: {total}")
