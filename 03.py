from utils import slurp

filedata = slurp("03.txt")


def part1(moves):
    houses = set()
    x, y = 0, 0
    houses.add((x, y))
    for move in moves:
        if move == "^":
            y += 1
        elif move == ">":
            x += 1
        elif move == "v":
            y -= 1
        elif move == "<":
            x -= 1
        houses.add((x, y))
    return len(houses)


def part2(moves):
    houses = set()
    houses.add((0, 0))
    positions = [[0, 0], [0, 0]]
    agent = 0
    for move in moves:
        if move == "^":
            positions[agent][1] += 1
        elif move == ">":
            positions[agent][0] += 1
        elif move == "v":
            positions[agent][1] -= 1
        elif move == "<":
            positions[agent][0] -= 1
        houses.add(tuple(positions[agent]))
        agent = (agent + 1) % 2
    return len(houses)


print("#--- Day 3: Perfectly Spherical Houses in a Vacuum: part1:", end=" ")

assert part1(">") == 2
assert part1("^>v<") == 4
assert part1("^v^v^v^v^v") == 2
print(part1(filedata))

print("#--- Day 3: Perfectly Spherical Houses in a Vacuum: part2:", end=" ")

assert part2("^v") == 3
assert part2("^>v<") == 3
assert part2("^v^v^v^v^v") == 11
print(part2(filedata))
