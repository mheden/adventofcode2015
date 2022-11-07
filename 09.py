from utils import slurp, unpack, BIGNUM
from itertools import permutations


def parse(distances):
    nodes = set()
    weights = {}
    for distance in distances:
        from_, _, to, _, dist = distance.split(" ")
        nodes.add(from_)
        nodes.add(to)
        if from_ not in weights:
            weights[from_] = {}
        if to not in weights:
            weights[to] = {}
        weights[from_][to] = int(dist)
        weights[to][from_] = int(dist)
    return nodes, weights



def part1(distances):
    nodes, weights = parse(distances)
    result = BIGNUM
    for route in permutations(nodes, len(nodes)):
        dist = 0
        start = route[0]
        for end in route[1:]:
            dist += weights[start][end]
            start = end
        result = min(dist, result)
    return result


def part2(distances):
    nodes, weights = parse(distances)
    result = 0
    for route in permutations(nodes, len(nodes)):
        dist = 0
        start = route[0]
        for end in route[1:]:
            dist += weights[start][end]
            start = end
        result = max(dist, result)
    return result


filedata = unpack(slurp("09.txt"))

print("#--- Day 9: All in a Single Night: part1:", end=" ")
assert (
    part1(
        [
            "London to Dublin = 464",
            "London to Belfast = 518",
            "Dublin to Belfast = 141",
        ]
    )
    == 605
)
print(part1(filedata))

print("#--- Day 9: All in a Single Night: part2:", end=" ")
assert (
    part2(
        [
            "London to Dublin = 464",
            "London to Belfast = 518",
            "Dublin to Belfast = 141",
        ]
    )
    == 982
)
print(part2(filedata))
