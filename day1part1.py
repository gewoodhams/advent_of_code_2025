zero = 0
current = 50

with open("day1part1.txt") as file:
    codes = file.read().splitlines()

for line in codes:
    direction = line[0]
    turn = int(line[1:])
    current += turn if (
            direction == 'R') \
        else -turn


    if current % 100 == 0:
        zero += 1

print(zero)