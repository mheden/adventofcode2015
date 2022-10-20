from utils import slurp, unpack

filedata = unpack(slurp("08.txt"))


def strlen(str):
    # strip trailing and ending "
    str = str[1 : len(str) - 1]
    len_ = 0
    i = 0
    while i < len(str):
        substr = str[i : i + 2]
        if substr == r"\\" or substr == r"\"":
            i += 2
        elif substr == r"\x":
            i += 4
        else:
            i += 1
        len_ += 1
    return len_


def part1(rows):
    code, len_ = 0, 0
    for row in rows:
        code += len(row)
        len_ += strlen(row)
    return code - len_


def encode(str):
    ret = ['"']
    for s in str:
        if s in ["\\", '"']:
            ret.append("\\")
        ret.append(s)
    ret.append('"')
    return "".join(ret)


def part2(rows):
    original, new = 0, 0
    for row in rows:
        original += len(row)
        newrow = encode(row)
        new += len(newrow)
    return new - original


print("#--- Day 8: Matchsticks: part1:", end=" ")
assert (
    part1(
        [
            r'""',
            r'"abc"',
            r'"aaa\"aaa"',
            r'"\x27"',
        ]
    )
    == 12
)
print(part1(filedata))

print("#--- Day 8: Matchsticks: part2:", end=" ")
assert (
    part2(
        [
            r'""',
            r'"abc"',
            r'"aaa\"aaa"',
            r'"\x27"',
        ]
    )
    == 19
)
print(part2(filedata))
