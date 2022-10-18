from utils import slurp

filedata = slurp("01.txt")


def part1(s):
    return s.count("(") - s.count(")")


def part2(s):
    floor = 0
    for i, instruction in enumerate(s):
        if instruction == "(":
            floor += 1
        if instruction == ")":
            floor -= 1
        if floor < 0:
            return i + 1


print("#--- Day 1: Not Quite Lisp: part1:", end=" ")

assert part1("(())") == 0
assert part1("()()") == 0
assert part1("(((") == 3
assert part1("(()(()(") == 3
assert part1("))(((((") == 3
assert part1("())") == -1
assert part1("))(") == -1
assert part1(")))") == -3
assert part1(")())())") == -3
print(part1(filedata))

print("#--- Day 1: Not Quite Lisp: part2:", end=" ")

assert part2(")") == 1
assert part2("()())") == 5
print(part2(filedata))
