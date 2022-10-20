from utils import slurp, unpack
from contextlib import suppress

filedata = unpack(slurp("07.txt"))


def part1(instructions):
    def process(wires, instructions):
        left = []
        for instruction in instructions:
            ins, wire = instruction.split(" -> ")
            ins = ins.split(" ")

            if len(ins) == 1:
                with suppress(ValueError):
                    wires[ins[0]] = int(ins[0])
            if len(ins) == 2:
                with suppress(ValueError):
                    wires[ins[1]] = int(ins[1])
            if len(ins) == 3:
                with suppress(ValueError):
                    wires[ins[1]] = int(ins[1])
                with suppress(ValueError):
                    wires[ins[2]] = int(ins[2])

            if len(ins) == 1 and ins[0] in wires:
                wires[wire] = wires[ins[0]]
            elif len(ins) == 2 and ins[1] in wires:
                wires[wire] = ~wires[ins[1]]
            elif len(ins) == 3 and ins[0] in wires and ins[2] in wires:
                x, op, y = ins
                if op == "AND":
                    wires[wire] = wires[x] & wires[y]
                elif op == "OR":
                    wires[wire] = wires[x] | wires[y]
                elif op == "LSHIFT":
                    wires[wire] = wires[x] << wires[y]
                elif op == "RSHIFT":
                    wires[wire] = wires[x] >> wires[y]
            else:
                left.append(instruction)

        for wire in wires:
            while wires[wire] < 0:
                wires[wire] += 0x10000
        return left

    wires = {}
    while len(instructions) > 0:
        instructions = process(wires, instructions)
    return wires


print("#--- Day 7: Some Assembly Required: part1:", end=" ")
wires = part1(
    [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i",
    ]
)
assert wires["d"] == 72
assert wires["e"] == 507
assert wires["f"] == 492
assert wires["g"] == 114
assert wires["h"] == 65412
assert wires["i"] == 65079
assert wires["x"] == 123
assert wires["y"] == 456
print(part1(filedata)["a"])

print("#--- Day 7: Some Assembly Required: part2:", end=" ")
for i, instruction in enumerate(filedata):
    if instruction.endswith("-> b"):
        filedata[i] = "3176 -> b"
print(part1(filedata)["a"])
