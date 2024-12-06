import os

DIRECTORY_PATH = os.path.abspath(os.path.join(__file__, "..", ".."))
FILE_NAME = "input.txt"

total = 0
with open(DIRECTORY_PATH + "\\" + FILE_NAME, "r") as file:
	for line in file:
		safe = True
		values = list(map(int, line.strip().split()))
		iterator = 0
		increasing = None
		while safe and iterator < len(values) - 1:
			value1 = values[iterator]
			value2 = values[iterator + 1]
			if increasing is None:
				if value1 == value2:
					safe = False
				else:
					increasing = value1 < value2
			else:
				if value1 == value2 or increasing != (value1 < value2) or abs(value1 - value2) > 3:
					safe = False
				iterator += 1
		if safe:
			total += 1

print(f"Total distance: {total}")
