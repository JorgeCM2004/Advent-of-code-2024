import os
from typing import Literal

DIRECTORY_PATH = os.path.abspath(os.path.join(__file__, "..", ".."))
FILE_NAME: Literal["example_P1.txt", "input.txt"] = "input.txt"

def process_line(line: str):
	total = 0
	sub_string = "mul("
	string_index = 0
	value1 = 0
	value2 = 0
	comma = False
	processed_at_least_one = False
	for char in line:
		if string_index >= len(sub_string):
			if not comma:
				if char == ',':
					comma = True
				else:
					try:
						value1 = value1 * 10 + int(char)
					except:
						value1 = 0
						string_index = 0
			else:
				if processed_at_least_one and char == ")":
					total += value1 * value2
					value1 = 0
					value2 = 0
					comma = False
					string_index = 0
				else:
					try:
						value2 = value2 * 10 + int(char)
						processed_at_least_one = True
					except:
						value1 = 0
						value2 = 0
						comma = False
						string_index = 0
		elif char == sub_string[string_index]:
			string_index += 1
		else:
			string_index = 0
	return total

total = 0
with open(DIRECTORY_PATH + "\\" + FILE_NAME, "r") as file:
	for line in file:
		total += process_line(line)

print(f"Multiplication result: {total}")
