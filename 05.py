from utils import slurp

filedata = slurp("05.txt")


def part1(strings):
    valid = 0
    for string in strings.split("\n"):
        vowels = (
            sum(
                string.count("a"),
                string.count("e"),
                string.count("i"),
                string.count("o"),
                string.count("u"),
            )
            >= 3
        )
        double = False
        for i in range(1, len(string)):
            if string[i - 1] == string[i]:
                double = True
        invalid = "ab" in string or "cd" in string or "pq" in string or "xy" in string
        if not invalid and vowels and double:
            valid += 1
    return valid


def part2(strings):
    return 0


print("#--- Day 5: Doesn't He Have Intern-Elves For This?: part1:", end=" ")

assert part1("ugknbfddgicrmopn") == 1
assert part1("aaa") == 1
assert part1("jchzalrnumimnmhp") == 0
assert part1("haegwjzuvuyypxyu") == 0
assert part1("dvszwmarrgswjxmb") == 0
print(part1(filedata))

print("#--- Day 5: Doesn't He Have Intern-Elves For This?: part2:", end=" ")

assert part2("qjhvhtzxzqqjkmpb") == 1
assert part2("xxyxx") == 1
assert part2("uurcxstgmygtbstg") == 0
assert part2("ieodomkazucvgmuy") == 0
print(part2(filedata))
