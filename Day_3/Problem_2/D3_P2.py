import os
from typing import Literal

DIRECTORY_PATH = os.path.abspath(os.path.join(__file__, "..", ".."))
FILE_NAME: Literal["example_P2.txt", "input.txt"] = "input.txt"

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

def clear_disables(line: str, status: Literal["continue", "erase"] = "continue"):
	line = list(line)
	enables = "do()"
	disables = "don't()"
	string_index = 0
	iterator = 0
	while iterator < len(line):
		char = line[iterator]
		if status == "continue":
			if string_index >= len(disables):
				status = "erase"
				string_index = 0
				iterator -= 1
			elif char == disables[string_index]:
				string_index += 1
			else:
				string_index = 0
			iterator += 1
		else:
			if string_index >= len(enables):
				status = "continue"
				string_index = 0
			elif char == enables[string_index]:
				string_index += 1
				line.pop(iterator)
			else:
				string_index = 0
				line.pop(iterator)
	return "".join(line), status

total = 0
with open(DIRECTORY_PATH + "\\" + FILE_NAME, "r") as file:
	status = "continue"
	for line in file:
		line, status = clear_disables(line, status)
		total += process_line(line)

print(f"Multiplication result: {total}")
