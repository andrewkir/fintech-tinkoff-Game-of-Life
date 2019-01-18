import random
import copy
import os
import time
import argparse

# parse args
parser = argparse.ArgumentParser()
parser.add_argument("--field", help="size of the field: NxN")
parser.add_argument("--gen", help="number of generations")
parser.add_argument("--sec", help="waiting time")
parser.add_argument("--inf", help="toggle infinite mode", action="store_true")
parser.add_argument("--key", help="toggle keyboard mode (press ENTER for next generation)", action="store_true")
args = parser.parse_args()

# default values
fieldSize = 5
generations = 5
seconds = 3
infinite = False
keyboardMode = False

# args processing
try:
    if args.field:
        fieldSize = int(str(args.field))
        if fieldSize <= 1:
            print('Incorrect field size, setting to 5')
            time.sleep(3)
            fieldSize = 5
except:
    pass

try:
    if args.gen:
        generations = int(str(args.gen))
        if generations < 1:
            print('Incorrect generations amount, setting to 5')
            time.sleep(3)
            generations = 5
except:
    pass

try:
    if args.sec:
        seconds = float(str(args.sec))
        if seconds < 0:
            print('Incorrect time amount, setting to 3')
            time.sleep(3)
            seconds = 3
except:
    pass

if args.inf:
    infinite = True

if args.key:
    keyboardMode = True


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Field:
    def __init__(self, field_size):
        self.size = fieldSize
        self.field = [[random.randint(0, 3) for i in range(fieldSize)] for _ in range(field_size)]

    def __repr__(self):
        res = ''
        for line in self.field:
            res += ' '.join(str(x) for x in line) + '\n'
        return res


def check_condition(tfield, target, i, j):
    count = 0
    if j - 1 >= 0 and tfield.field[i][j - 1] == target:
        count += 1
    if j - 1 >= 0 and i - 1 >= 0 and tfield.field[i - 1][j - 1] == target:
        count += 1
    if i - 1 >= 0 and tfield.field[i - 1][j] == target:
        count += 1
    if i - 1 >= 0 and j + 1 < tfield.size and tfield.field[i - 1][j + 1] == target:
        count += 1
    if j + 1 < tfield.size and tfield.field[i][j + 1] == target:
        count += 1
    if j + 1 < tfield.size and i + 1 < tfield.size and tfield.field[i + 1][j + 1] == target:
        count += 1
    if i + 1 < tfield.size and tfield.field[i + 1][j] == target:
        count += 1
    if i + 1 < tfield.size and j - 1 >= 0 and tfield.field[i + 1][j - 1] == target:
        count += 1
    return count


# 0 - nothing
# 1 - fish
# 2 - shrimp
# 3 - rock
field = Field(fieldSize)
generation = 0

cls()
print(field)
print(f"Generation: {generation}\n")
if not keyboardMode:
    time.sleep(seconds)
else:
    input('Press Enter to continue...\nCTRL+C to stop')
cls()

while generation <= generations or infinite:
    check = copy.deepcopy(field)
    for i in range(field.size):
        for j in range(field.size):
            # check fish
            if field.field[i][j] == 1 and (
                    check_condition(field, 1, i, j) >= 4 or check_condition(field, 1, i, j) < 2):
                check.field[i][j] = 0

            if field.field[i][j] == 0 and (
                    field.field[i][j] == 0 and check_condition(field, 1, i, j) == 3):
                check.field[i][j] = 1

            # check shrimp
            if field.field[i][j] == 2 and (
                    check_condition(field, 2, i, j) >= 4 or check_condition(field, 2, i, j) < 2):
                check.field[i][j] = 0

            if field.field[i][j] == 0 and (
                    field.field[i][j] == 0 and check_condition(field, 2, i, j) == 3):
                check.field[i][j] = 2

    field = copy.deepcopy(check)
    generation += 1

    print(field)
    print(f"Generation: {generation}\n")
    if not keyboardMode:
        time.sleep(seconds)
    else:
        input('Press Enter to continue...\nCTRL+C to stop')
    cls()
print(field)
